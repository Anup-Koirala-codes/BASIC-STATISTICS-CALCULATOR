def calc():
    
    # STEP 1: Get class interval settings from user
    
    class_start  = int(input("Enter a lowest value of first class : "))
    class_end    = int(input("Enter a highest value of last class (3 digit number doesnt look nice): "))
    class_width  = int(input("Enter a value of class interval : "))

    frequencies      = []   # f  — frequency of each class
    class_boundaries = []   # stores [lower, upper] bounds for each class

     
    # STEP 2: Collect frequency for each class
     
    print("Class (X)    |   frequency (f) \t|")

    current = class_start
    num_classes = 0

    while current != class_end:
        upper = current + class_width
        print(f"{current} - {upper}", end="\t     |\t\t")

        freq = int(input())
        frequencies.append(freq)
        class_boundaries.append([current, upper])

        current += class_width
        num_classes += 1

    total_frequency = sum(frequencies)  # N — total number of observations

     
    # STEP 3: Compute per-class derived values
     
    midpoints          = []   # m    — midpoint of each class
    freq_x_midpoint    = []   # fm   — frequency × midpoint
    midpoint_squared   = []   # m²   — midpoint squared
    freq_x_mid_sq      = []   # fm²  — frequency × midpoint²
    cumulative_freq    = []   # cf   — running cumulative frequency

    for i in range(num_classes):
        lower, upper = class_boundaries[i]

        mid = (lower + upper) / 2
        midpoints.append(mid)
        freq_x_midpoint.append(frequencies[i] * mid)
        midpoint_squared.append(mid * mid)
        freq_x_mid_sq.append(frequencies[i] * mid * mid)

        # Cumulative frequency: add current freq to previous cumulative
        if i == 0:
            cumulative_freq.append(frequencies[i])
        else:
            cumulative_freq.append(cumulative_freq[i - 1] + frequencies[i])

     
    # STEP 4: Mean and Standard Deviation
     
    sum_fm   = sum(freq_x_midpoint)   # Σfm
    sum_fm2  = sum(freq_x_mid_sq)     # Σfm²

    mean               = sum_fm / total_frequency
    variance           = sum_fm2 / total_frequency - mean ** 2
    standard_deviation = variance ** 0.5

     
    # STEP 5: Median (interpolation formula)
     
    median_position = total_frequency / 2
    median = class_boundaries[0][0]  # default fallback

    for i in range(num_classes):
        if median_position <= cumulative_freq[i]:
            prev_cf = cumulative_freq[i - 1] if i > 0 else 0
            median = class_boundaries[i][0] + class_width * ((median_position - prev_cf) / frequencies[i])
            break

     
    # STEP 6: Quartiles Q1 and Q3 (interpolation)
     
    q1_position = total_frequency / 4
    q1 = class_boundaries[0][0]  # default fallback

    for i in range(num_classes):
        if q1_position <= cumulative_freq[i]:
            prev_cf = cumulative_freq[i - 1] if i > 0 else 0
            q1 = class_boundaries[i][0] + class_width * ((q1_position - prev_cf) / frequencies[i])
            break

    q3_position = 3 * total_frequency / 4
    q3 = class_boundaries[0][0]  # default fallback

    for i in range(num_classes):
        if q3_position <= cumulative_freq[i]:
            prev_cf = cumulative_freq[i - 1] if i > 0 else 0
            q3 = class_boundaries[i][0] + class_width * ((q3_position - prev_cf) / frequencies[i])
            break

     
    # STEP 7: Mode (grouping / interpolation formula)
     
    modal_frequency = max(frequencies)  # highest frequency value
    mode = class_boundaries[0][0]       # default fallback

    for i in range(num_classes):
        if modal_frequency == frequencies[i]:
            if i == num_classes - 1:
                # Modal class is the last class — use lower boundary directly
                mode = class_boundaries[i][0]
            else:
                prev_f = frequencies[i - 1] if i > 0 else 0
                next_f = frequencies[i + 1]
                # Standard mode interpolation: L + h * (f1 - f0) / (2f1 - f0 - f2)
                mode = class_boundaries[i][0] + class_width * (
                    (modal_frequency - prev_f) /
                    (modal_frequency - prev_f + modal_frequency - next_f)
                )
            break

     
    # STEP 8: Quartile Deviation
     
    quartile_deviation             = (q3 - q1) / 2
    coeff_quartile_deviation       = (q3 - q1) / (q3 + q1)

     
    # STEP 9: Coefficient of Variation / Standard Deviation
     
    coeff_of_variation             = (standard_deviation / mean) * 100  # as percentage
    coeff_of_standard_deviation    = standard_deviation / mean

     
    # STEP 10: Mean Deviation from Mean and Median
     
    dev_from_mean    = []   # |m - Mean|    for each class
    fdev_from_mean   = []   # f × |m - Mean|
    dev_from_median  = []   # |m - Median|
    fdev_from_median = []   # f × |m - Median|

    for i in range(num_classes):
        abs_dev_mean   = abs(midpoints[i] - mean)
        abs_dev_median = abs(midpoints[i] - median)

        dev_from_mean.append(abs_dev_mean)
        fdev_from_mean.append(frequencies[i] * abs_dev_mean)
        dev_from_median.append(abs_dev_median)
        fdev_from_median.append(frequencies[i] * abs_dev_median)

    mean_deviation_from_mean    = sum(fdev_from_mean) / total_frequency
    mean_deviation_from_median  = sum(fdev_from_median) / total_frequency
    coeff_md_from_mean          = mean_deviation_from_mean / mean
    coeff_md_from_median        = mean_deviation_from_median / median

     
    # OUTPUT SECTION
     

    divider = "_" * 126

    # ── Table 1: Main frequency distribution table ──
    print(divider)
    print("\n")
    print("x  \t|\tf\t|\tcf\t|\tm\t|\tfm\t|\tm²\t|\tfm²\t|")
    print(divider)
    for i in range(num_classes):
        lower, upper = class_boundaries[i]
        print(f"{lower} - {upper}\t|\t{frequencies[i]}\t|\t{cumulative_freq[i]}\t|\t{midpoints[i]}\t|\t{freq_x_midpoint[i]}\t|\t{midpoint_squared[i]}\t|\t{freq_x_mid_sq[i]}\t|")
    print(divider)
    print(f"Total\t     N={total_frequency}\t\t\t\t\t    Efm={sum_fm}\t\t\t  Efm²={sum_fm2}")
    print(divider)

    # ── Central Tendency ──
    print("\n")
    print(f"Mean = {mean:.3f}")
    print(f"Mode = {mode:.3f}")
    print("\n")

    # ── Dispersion ──
    print(divider)
    print("\n")
    print(f"Standard Deviation = {standard_deviation:.3f}")
    print(f"Coefficient of Variation = {coeff_of_variation:.3f}%")
    print(f"Coefficient of Standard Deviation = {coeff_of_standard_deviation:.3f}")
    print(f"Variance = {variance:.3f}")
    print("\n")

    # ── Quartiles ──
    print(divider)
    print(f"position of Q1 = {q1_position:.3f}")
    print(f"Q1 = {q1:.3f}")
    print("\n")
    print(divider)
    print("\n")
    print(f"position of median = {median_position:.3f}")
    print(f"Median = {median:.3f}")
    print("\n")
    print(divider)
    print("\n")
    print(f"position of Q3 = {q3_position:.3f}")
    print(f"Q3 = {q3:.3f}")
    print("\n")
    print(divider)
    print("\n")
    print(f"Quartile Deviation = {quartile_deviation:.3f}")
    print(f"Coefficient of Quartile Deviation = {coeff_quartile_deviation:.3f}")
    print("\n")

    # ── Table 2: Mean Deviation table ──
    print(divider)
    print("x  \t|\tf\t|\tm\t|    |m-Mean|   |       f|m-Mean|       |   |m-Median|  |    f|m-Median|\t|")
    print(divider)
    for i in range(num_classes):
        lower, upper = class_boundaries[i]
        print(
            f"{lower} - {upper}\t|\t{frequencies[i]}\t|\t{midpoints[i]}\t|"
            f"\t{dev_from_mean[i]:.3f}\t|\t{fdev_from_mean[i]:.3f}\t\t|"
            f"\t{dev_from_median[i]:.3f}\t|\t{fdev_from_median[i]:.3f}\t\t|"
        )
    print(divider)
    print(f"Total\t  |   N={total_frequency}\t\t\t\t\t   |  Ef|m-Mean|={sum(fdev_from_mean):.3f}\t\t\t|  Ef|m-Median|={sum(fdev_from_median):.3f}")
    print(divider)

    # ── Mean Deviation Results ──
    print("\n")
    print(f"Mean Deviation from Mean = {mean_deviation_from_mean:.3f}")
    print(f"Coefficient of MD from Mean = {coeff_md_from_mean:.3f}")
    print(f"Mean Deviation from Median = {mean_deviation_from_median:.3f}")
    print(f"Coefficient of MD from Median = {coeff_md_from_median:.3f}")
    print("\n")
    print(divider)
    print("\n")


calc()