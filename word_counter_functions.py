def get_sentence_input() -> str:
    """
    Prompt the user to enter a sentence.

    Returns:
        str: The user's input as a string.
    """
    return input("Enter a sentence: ").strip()


def count_words(sentence: str) -> int:
    """
    Count the number of words in a given sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        int: The number of words in the sentence.
    """
    words = sentence.split()
    return len(words)


# Main Program Flow
if __name__ == "__main__":
    sentence = get_sentence_input()
    word_count = count_words(sentence)
    print(f"The sentence has {word_count} words.")