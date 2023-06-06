# Cosine Similarity (Distance Algorithm) in Python 3+

> This repository is purely for reference and is illustrative in it is purpose. This is one of the many ways of implementing this algorithm, but represents a vanilla implementation without any additional packages.


This project illustrates an implementation of the distance algorithm [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity) in Python. The Cosine Similarity is a distance algorithm that determines how "similar" two non-zero vectors are when compared. In the case of this implementation, phrases or sentences are used as AB inputs instead of non-zero vectors alone.

Phrases or sentences are converted into vectors by splitting the words apart counting the number of occurances in each phrase or sentence to create vectors. These vectors are then compared using the cosine similarity equation.

## Example

* Sentence A : "My cat has fleas in its fur."
* Sentence B : "My cat has ticks in the fur on its head."


||my|cat|has|fleas|ticks|in|its|the|fur|on|head|
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Stc A|1|1|1|1|0|1|1|0|1|0|0
|Stc B|1|1|1|0|1|1|1|1|1|1|1

### Results in 0.72 or 72% alike
Re-iterating that this is a vanilla implementation that does not include any weighting, libraries, stop word, or any methods of finding "meaning" in a phrase or sentence.


> **IMPORTANT**
>
> This algorithm was authored to be *readable* as to the steps to achieve consistant and expected NYSIIS codes given the specification provided. 
 **This code can be refactored to be more compact and performant if needed.**


## Prerequisites

Before you continue, ensure you have met the following requirements:

* Python 3 installed
* PyTest installed (to run the unit tests if need be)

## Running / Testing

* Run **pytest** from the command line 


## Notes

* This repository is heavily commented to provide context as to what and why, if in VS Code feel free to collapse all comments if they are obtrusive
    * On Mac -> Press <kbd>&#8984;</kbd> + <kbd>K</kbd> then <kbd>&#8984;</kbd> + <kbd>/</kbd> 
    * On Windows & Linux -> Press <kbd>Ctrl</kbd> + <kbd>K</kbd> then <kbd>Ctrl</kbd> + <kbd>/</kbd> 

