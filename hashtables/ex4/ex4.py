def has_negatives(a):

# I will call my dictionary variable 'hashtable' to make me feel better.

    hashtable = {}
    result = []

    for i in a:
        if i != 0:

            # Build dictionary
            hashtable[i] = True

            # Check dictionary for desired values
            if hashtable.get(-i, None) is not None:

                # Add values if they are desired
                result.append(abs(i))

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
