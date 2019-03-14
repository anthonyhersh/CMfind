// Under Construction

// CMfind will be a conceptual metaphor (CM) detector. As of early 2019, we have not yet found a solution that would be helpful in manual detection.

// When ready, CMfind will first be used to detect CM in The Lotus Sutra in English, then Chinese, then ancient Chinese.

// In a nutshell, we will find a way to train a neural network (NN) algorithm to detect CMs, then in a completely seperate step, have it analyze The Lotus Sutra (LS), chapter 25. If it can speed up the efficiency of CM detection it will be improved, then run on the entire LS text. If that sees success, we will try to add the Chinese language function and repeat the process (ch. 25, then entire text). 

// https://github.com/keras-team/keras/tree/master/examples - Good place to start without having to directly use TensorFlow
//    ~/imdb_lstm.py looks promising

// More detail on how to implement CM will come as the code is completed. At first it will be solely a python script run via command-line. 

// Only after a prototype is viable do I (snake-arms) intend on building a GUI for manual analysis, but if someone else wants to build that it would help us test the scripts.

// http://nlpprogress.com/ - which links to a paper that links to:
//    https://github.com/ytsvetko/metaphor - Metaphor detection, well documented, plus a couple clean metaphor lists (Adj-Noun, and SVO)
