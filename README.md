# ColourBot
This has been done in collaboration with https://github.com/Jackson-Greenee

A discord bot written within python that allows users to change their name colour
If you wish to use this code simply add your own bot token.

## To run
Requires python3

`python3 colourbot.py`
## Prefix
"!" before command Example: "!help"
## Commands
### help
`Help command that lists how to use bot and lists colours currently added in colours list`
### colour
`!colour <colour code/colour name"> to assign colour to user`

## Notes
If you would like to add more colours to the colours list, you can do so by manually adding more into the colour map/dictionary at the top of the code with name and the hex code in the same format as the other colours

Discord uses the colour of the highest role of the user, any role higher than the role assigned by the bot will be the visible colour
The easiest way to avoid issues with this is to have no colours for any roles except for the ones that will be made by the bot. 

You can check this by making sure all non colour-bot roles are set to default as shown below:
![Image of Default Discord Color Role](https://user-images.githubusercontent.com/65131267/81722025-62734600-94b3-11ea-8d68-daef0855f660.png)
