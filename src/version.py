import discord
import sys
import os
import platform

def getOSVersion():
    if platform.version() >= "10.0.22000" and platform.release() == "10" and platform.system() == "Windows":
        return f"Windows 11 (build {platform.version()}) {platform.architecture()[0]}"
    return f"{platform.system()} {platform.release()} (build {platform.version()}) {platform.architecture()[0]}"

def getDiscordVersion():
    return f"{discord.version_info.major}.{discord.version_info.minor}.{discord.version_info.micro} {discord.version_info.releaselevel}"

def getPythonVersion():
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} {sys.version_info.releaselevel}"