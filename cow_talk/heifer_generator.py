from cow import Cow
from dragon import Dragon
from ice_dragon import IceDragon


def get_cows():
    cow_names = ["heifer", "kitteh"]

    quote_lines = "    \\\n"
    quote_lines += "     \\\n"
    quote_lines += "      \\\n"

    cowImages = [
        "        ^__^\n"
        + "        (oo)\\_______\n"
        + "        (__)\\       )\\/\\\n"
        + "            ||----w |\n"
        + "            ||     ||\n",
        "       (\"`-'  '-/\") .___..--' ' \"`-._\n"
        + "         ` *_ *  )    `-.   (      ) .`-.__. `)\n"
        + "         (_Y_.) ' ._   )   `._` ;  `` -. .-'\n"
        + "      _.. `--'_..-_/   /--' _ .' ,4\n"
        + "   ( i l ),-''  ( l i),'  ( ( ! .-'\n",
    ]

    dragon_names = ["dragon", "ice-dragon"]
    dragon_types = [Dragon, IceDragon]

    dragon_image = (
        "           |\\___/|       /\\  //|\\\\\n"
        + "           /0  0  \\__   /  \\// | \\ \\\n"
        + "          /     /  \\/_ /   //  |  \\  \\\n"
        + "          \\_^_\\'/   \\/_   //   |   \\   \\\n"
        + "          //_^_/     \\/_ //    |    \\    \\\n"
        + "       ( //) |        \\ //     |     \\     \\\n"
        + "     ( / /) _|_ /   )   //     |      \\     _\\\n"
        + "   ( // /) '/,_ _ _/  ( ; -.   |    _ _\\.-~       .-~~~^-.\n"
        + " (( / / )) ,-{        _      `.|.-~-.          .~         `.\n"
        + "(( // / ))  '/\\      /                ~-. _.-~      .-~^-.  \\\n"
        + "(( /// ))      `.   {            }                 /      \\  \\\n"
        + " (( / ))     .----~-.\\        \\-'               .~         \\  `.   __\n"
        + "            ///.----..>        \\            _ -~            `.  ^-`  \\\n"
        + "              ///-._ _ _ _ _ _ _}^ - - - - ~                   `-----'\n"
    )

    cows = [None] * (len(cow_names) + len(dragon_names))
    # add the 'regular' cows
    num_regular = len(cow_names)
    for index in range(num_regular):
        cows[index] = Cow(cow_names[index])
        cows[index].set_image(quote_lines + cowImages[index])

    # add the dragons
    for index in range(len(dragon_names)):
        cows[num_regular + index] = dragon_types[index](
            dragon_names[index], quote_lines + dragon_image
        )

    return cows
