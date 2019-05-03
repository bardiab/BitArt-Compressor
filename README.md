## BitArt Encoder/Decoder 

Encoding/Decoding functions for ascii images in order to efficiently prepare
them for data transport.

### Prerequisites

Your machine must be running python3, script will not run correctly on anything below python3.

### Installing

Download and unzip the .zip file. There are two main files. Before running either, ensure that you have a valid bitmap image titled 'data.txt' located in the directory. This file contains the image that will be encoded/decoded.

In order to encode/decode images, run:

```
python compress.py
```

In order to run the tests:

```
python testing.py
```

### Requirements

- **Completeness**: Successfully encodes/decodes the given image
- **Correctness**: Functionality works as expected
- **Reasoning**: In order to compress bitmap images, I decided on two main
strategies while parsing through the .txt file line by line. First, I stored the number of whitespaces per line as an int. Second, I compressed the remaining part of the string by replacing repeated characters with the character followed by the number of times it was repeated. Using these two techniques, I stored the data
for each line as a tuple into the 'encoded.txt' file. In order to decode this file,
I used regex parsing in order to parse through the tuples and uncompress both the
number of whitespaces and the compressed characters. These two methods seemed like
the most efficient and practical methods in order to quickly and efficiently
compress images while preserving the input. Using this method, I was able to compress the original image by 65%.


### Built With

* [Atom](https://atom.io) - TextEditor used
