def freq_analysis(input_list):
    freq = {}
    for i in input_list:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq