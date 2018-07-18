# Adventure POC

This is a basic text-based adventure game made by some friends who wanted to explore Python and the world of game making.

## Getting Started

To play the game, just run "adventure.py" from any terminal.

```
> adventure.py
==[ Outside ]==
You are a bad ass holy inquisitor, here to banish evil.
You carry with you a crossbow, a holy cross, a vial of holy water and a vial of flammable oil.
Other than your wits these are your only weapons.
You stand before the main entrance to the cursed dungeon where evil lurks.
The large wooden door before you seems old and rotten

What do you do?
please select one of the choices:
 - [1] : Open the door slowly
 - [2] : Kick down the door!
Your choice?: 
```

### Prerequisites

You must have Python installed, (tested with version 2.7.11)

## Running tests and logging and debugging

 - There is a test script `test-adventure.py` (not implemented yet)
 - There is basic logging. use `--log` to enable logging, and `--log-file` to specify a file to write logs to.
 - You can enable debug mode by launching the game with `--debug` or by writing `debug-mode` at any choice prompt. 


```
> adventure.py --log  --log-file=C:/tmp/adventure.log --debug
```

## Contributing

We are not actively taking contributions at the moment. This is a personal project between some friends.

However, if you would like to contribute please feel free to fork and make a pull request, but we would rather you discussed with us first.

## Authors / Creators / Credits

* **Inbar Rose** - *Code Master and Architect* - [InbarRose](https://github.com/InbarRose)
* **Alon Cang** - *Game Design and Text* - [InbarRose](https://github.com/AlonCang)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Background (for the curious)

We were a bunch of friends (first we were more, now we are less) who wanted to make a simple text-based adventure game together using Python. Eventually we had the idea for this game, something without too mcuh ambition that could be completed in a timely manner that would help us identify methodologies of building a game, coding together in a team, and serve as a base for a later game we or game system we may develop. 

Inbar is the the one with the Python experience and wherewithal to pull us all together and start us down this path. But we are all avid gamers and RPG lovers.

In the future, we plan to have the "story" be a module that can be loaded simply, so that the games "engine" can be used to tell many stories. But maybe that is a bit too ambitious for right now! 
