# CrossJoin-AESO Discord Bot

### Prelude:
This is my first experience using both the discord.py library to make a basic discord app as well as my first time utilizing the AESO API. In essence what it currently does is let you say !CrossJoin then type a command and sometimes extension to run a command that the bot uses to call the API and process it into usable information.

### How to use:

#### Setting up .env:
- Create `.env` file in project root. 
- Add the following values to your file:
  - `AESO_API_KEY`: Required for using AESO API. You can sign-up and get your API key on the [AESO developers portal](https://developer-apim.aeso.ca/).
  - `DISCORD_KEY`: Required to connect with your bot on Discord. You can find this on the [applications section of the Discord developers portal](https://discord.com/developers/applications). 

#### Docker (recommended):
- Run `docker compose --env-file ./.env up`.

#### Systemd:
- Place or link the file located at `./config/CrossJoin.service` in `/etc/systemd/system/`.
- If you are using `venv`, make sure to change the python executable location in `ExecStart`.

#### Using the bot: 
- Add the bot to your server.
- Bot supports Discord command notation (`/` commands). 
- Run `/help` for help.

### Future Additions:
- [x] Add in graph and chart visualizations.
- [x] Switch to using the discord `/` command notation.
- [ ] Cleanup and refinement of some parts of the system.
- [ ] Cleanup UI, further integrate into discords modern bot UI standards.
- [x] Integrate road reports into the bot if possible through their APIs.
  - [x] 511 Alberta.
    - [x] 511 Cameras.
    - [x] 511 Road conditions.

### Contributing Guidelines:
1) Check to see if something you would like to add already has a feature branch. If it does then go and get involved in the conversation there to see if your ideas can be implemented.
2) If there is an addition you would like to make to the bot, feel free to start making a feature branch and explain the purpose of that feature in the branch.

### Contributors:
<a href="https://github.com/SouthAlbertaAI/CrossJoin-AESO/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=SouthAlbertaAI/CrossJoin-AESO" />
</a>

### License:
This project is licensed under [The Clear BSD License](https://spdx.org/licenses/BSD-3-Clause-Clear.html).
