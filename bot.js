const Discord = require("discord.js");
const client = new Discord.Client();
const prefix = "*";

client.on("ready", ()=>{
    console.log(`${client.user.tag} connected to Discord`);
});

client.on("guildMemberAdd", member =>{
    member.roles.add(member.guild.roles.cache.find(role => role.name == "ROLENAME"), "auto added.");
	console.log(`Role added to ${member.user.tag}`);
  })
client.login("BOT_TOKEN")