# Helpful Prompt Engineering Tips


## Variable names
Use descriptive variable names to make your intentions clear.

    totalSampleCount = 1000


## Method Signatures
Define method signatures with unambiguous parameter names and types.

    double calculateAverageSampleSize(unsigned long samples[], size_t size)

## Show examples

    int samples[] = {1, 2, 3, 4, 5};
    double average = calculateAverageSampleSize(samples, 5);
    printf("Average: %f\n", average);

## Naming Conventions
Maintain consistent naming conventions for variables and functions.

    i.e. using camelCase for variable names consistancy

## Input/Output Format
Describe the expected input and output formats.

    Write a function 'palindrome' that takes an array of strings 'words' as input and returns true if a palindrome is found.

## Error Handling
Specify error handling scenarios.

    Exit where the input is NULL and throw an exception if the input out of range [min, max] inclusive.

## Control Structures
Describe control flow structures.

    Write a while loop to print the first 'n' values in the fibonnaci sequence.
