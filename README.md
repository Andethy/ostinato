# Ostinato

_To do: One or two lines about what the project can do._

## Introduction

_To do: provide an overview and description of high-level functionality and technologies utilized._

## Table of Contents

- [Introduction](#introduction)
- [Core Module](#core-module)
  - [gpt](#gpt)
  - [midi](#midi)
  - [audio](#audio)
  - [Genre-specific Classes](#genre-specific-classes)
- [API](#api)
- [Frontend](#frontend)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## Core Module

The Core module is the central pillar of this application, providing the fundamental mechanisms that power the system's unique capabilities. Accessible exclusively by the manager, the Core module synergizes its operations through three specialized submodules to execute a sophisticated conversion process. Furthermore, it encompasses a series of genre-specific classes designed to handle nuanced variations associated with different musical genres.

### gpt

The `gpt` submodule acts as the creative engine, leveraging advanced algorithms to craft a diverse array of completion responses. This process involves the generation of modelled notes and chords, which are subsequently translated into numerical data for additional processing. The intricate architecture of this submodule allows for the nuanced handling of musical information, forming the bedrock upon which subsequent conversion steps are performed.

### midi

Operating in perfect concert with the `gpt` submodule, the `midi` submodule serves a pivotal role in transmuting the raw, numerical representations of notes into structured musical data. This transformation involves complex mathematical computations, the result of which are rich, MIDI-formatted wrapper classes and score files. These elements are foundational in the construction of coherent musical tracks.

### audio

The `audio` submodule is the final stage in the conversion process, where it interprets and encodes the information assembled by the MIDI module into tangible audio files. These files, known as stems, are rendered in the universally compatible mp3 format. This module is meticulously engineered to map MIDI data to corresponding audio samples, overlaying sounds with precise timing to maintain tempo integrity, thereby producing a seamless auditory experience.

### Genre-specific Classes

In addition to the primary submodules, the Core module features a comprehensive suite of classes tailored to various musical genres. These classes are intrinsic to the system's ability to manage genre-specific peculiarities, ensuring accurate and representative audio output across a diverse musical spectrum.

## API

_To do: Provide an overview of the backend part of the application._

## Frontend

_To do: Provide an overview of the frontend part of the application._

## Installation

This is a relatively simple package to install; however, installation of [ffmpeg](https://ffmpeg.org/) is required. 
If on MacOS, I would recommend having [homebrew](https://brew.sh/) installed.
If on Windows, [follow this tutorial](https://phoenixnap.com/kb/ffmpeg-windows).

### Installation for MacOS
```bash
# clone the repository to your local machine
git clone https://github.com/andethy/ostinato.git

# navigate to the project's directory
cd ostinato

# install the dependencies
brew install ffmpeg
pip install -r requirements.txt
```

### Installation for Windows
```bash
# clone the repository to your local machine
git clone https://github.com/andethy/ostinato.git

# navigate to the project's directory
cd ostinato

# install the dependencies
pip install -r requirements.txt
```

## Usage

_Coming soon_

## Contributors

- Jack
- Hamza
- Hamzah
- Shayan

## License

_Information about the project's license._

```plaintext
Distributed under the AGPL-3.0 License. See `LICENSE` for more information.
```

## Contact

_Jack Hayley: [jack@bbadlands.com](mailto:jack@bbadlands.com)_

_Project Link: [https://github.com/andethy/ostinato](https://github.com/andethy/ostinato)_

## Acknowledgments

_In progress._

---

