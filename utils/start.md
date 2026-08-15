tw-make custom --force --theme house --world-size 1 --nb-objects 2 --seed 1234 --output tw_games/custom_2room.z8

tw-play tw_games/custom_1room.z8 --viewer

cd ~/TextWorld4Bash

python scripts/tw-make custom --force --theme ukrhouse --world-size 1 --nb-objects 2 --seed 1234 --output tw_games/custom_5room.z8

python scripts/tw-play tw_games/custom_5room.z8


