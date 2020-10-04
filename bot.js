const Discord = require("discord.js");
const client = new Discord.Client();

rolename = 'ROLENAME'
bot_token = 'BOT_TOKEN'

client.on("ready", ()=>{
    console.log(`${client.user.tag} connected to Discord`);
});

client.on("guildMemberAdd", member =>{
    member.roles.add(member.guild.roles.cache.find(role => role.name == rolename), "auto added.");
	console.log(`Role added to ${member.user.tag}`);
  })
client.login(bot_token)
