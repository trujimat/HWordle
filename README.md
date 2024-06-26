# HWordle

#### This project aims to solve the game [wordle](https://www.nytimes.com/games/wordle/index.html) using information theory.

## Requirements

This project has been tested on Ubuntu 22.04 with Python 3.10.12, but it should work on any Linux system with Python 3 or later.

To install the necessary Python packages listed in the `requirements.txt` file, navigate to the root directory of the project and run:

```bash
pip3 install -r requirements.txt
```

Alternatively, you can use Docker to build the project image. From the root directory of the project, run:

```bash
docker build .
```

For this, you need to have Docker installed on your machine.

## Run the Project

### Normal Running

To run the project, navigate to the root directory of the project and execute the following command:

```bash
python3 test_orchestrator.py {selected_word_to_guess} {number_of_processes}
```

Where `selected_word_to_guess` is the word that the project will attempt to guess, and `number_of_processes` is the number of processes the project will use to guess the word. By default, the number of processes is 1. Using a higher `number_of_processes` value will make the program finish earlier but will consume more resources.

### Docker running 

If you have built a Docker image for the project, run the following command:

```bash
docker run {image_id} {selected_word_to_guess} {number_of_processes}
```

Where `image_id` is the ID of the Docker image you built, `selected_word_to_guess` is the word that the project will attempt to guess, and `number_of_processes` is the number of processes the project will use to guess the word. By default, the number of processes is 1. Using a higher `number_of_processes` value will make the program finish earlier but will consume more resources.
