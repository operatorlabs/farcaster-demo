from langchain.tools import BaseTool
from typing import Any, Optional
import os
from dotenv import load_dotenv
import Levenshtein

channels = [
    {
        "name": "Neynar",
        "parent_url": "chain://eip155:1/erc721:0xd4498134211baad5846ce70ce04e7c4da78931cc",
        "channel_id": "neynar"
    },
    {
        "name": "FWB Fest",
        "parent_url": "https://fest.fwb.help",
        "channel_id": "fwb-fest"
    },
    {
        "name": "Welcome",
        "parent_url": "chain://eip155:7777777/erc721:0x8f0055447ffae257e9025b781643127ca604baaa",
        "channel_id": "welcome"
    },
    {
        "name": "GM",
        "parent_url": "chain://eip155:7777777/erc721:0x5556efe18d87f132054fbd4ba9afc13ebb1b0594",
        "channel_id": "gm"
    },
    {
        "name": "Farcaster",
        "parent_url": "chain://eip155:7777777/erc721:0x4f86113fc3e9783cf3ec9a552cbb566716a57628",
        "channel_id": "farcaster"
    },
    {
        "name": "/dev",
        "parent_url": "chain://eip155:1/erc721:0x7dd4e31f1530ac682c8ea4d8016e95773e08d8b0",
        "channel_id": "farcaster-dev"
    },
    {
        "name": "Warpcast",
        "parent_url": "chain://eip155:7777777/erc721:0x10a77f29a6bbeae936f3f27cd60546072dae4e41",
        "channel_id": "warpcast"
    },
    {
        "name": "EVM",
        "parent_url": "chain://eip155:1/erc721:0x37fb80ef28008704288087831464058a4a3940ae",
        "channel_id": "evm"
    },
    {
        "name": "zk",
        "parent_url": "chain://eip155:7777777/erc721:0xec30bb189781bbd87478f625d19d9deeeb771964",
        "channel_id": "zk"
    },
    {
        "name": "OP Stack",
        "parent_url": "https://www.optimism.io",
        "channel_id": "op-stack"
    },
    {
        "name": "Memes",
        "parent_url": "chain://eip155:1/erc721:0xfd8427165df67df6d7fd689ae67c8ebf56d9ca61",
        "channel_id": "memes"
    },
    {
        "name": "News",
        "parent_url": "chain://eip155:7777777/erc721:0x3cf3d6a6bcac3c60f3bb59fdd641b042102bb488",
        "channel_id": "news"
    },
    {
        "name": "Ethereum",
        "parent_url": "https://ethereum.org",
        "channel_id": "ethereum"
    },
    {
        "name": "Bitcoin",
        "parent_url": "https://bitcoin.org",
        "channel_id": "bitcoin"
    },
    {
        "name": "Solana",
        "parent_url": "https://solana.com",
        "channel_id": "solana"
    },
    { "name": "Tezos", "parent_url": "https://tezos.com", "channel_id": "tezos" },
    {
        "name": "Quilibrium",
        "parent_url": "https://www.quilibrium.com",
        "channel_id": "quilibrium"
    },
    {
        "name": "AI",
        "parent_url": "chain://eip155:7777777/erc721:0x5747eef366fd36684e8893bf4fe628efc2ac2d10",
        "channel_id": "ai"
    },
    {
        "name": "Design",
        "parent_url": "chain://eip155:7777777/erc721:0x22be981fb87effbe6780b34a6fe1dfc14a00ec8e",
        "channel_id": "design"
    },
    {
        "name": "Podcasts",
        "parent_url": "chain://eip155:1/erc721:0xdf3abf79aedcc085e9a41a569964e9fb53f33728",
        "channel_id": "podcasts"
    },
    {
        "name": "Food",
        "parent_url": "chain://eip155:1/erc721:0xec0ba367a6edf483a252c3b093f012b9b1da8b3f",
        "channel_id": "food"
    },
    {
        "name": "Books",
        "parent_url": "chain://eip155:1/erc721:0xc18f6a34019f5ba0fc5bc8cb6fe52e898d6bbbee",
        "channel_id": "books"
    },
    {
        "name": "Screens",
        "parent_url": "chain://eip155:1/erc721:0xc4934dbb7a71f76e4068cd04fade20ad6c0023dd",
        "channel_id": "screens"
    },
    {
        "name": "Fitness",
        "parent_url": "chain://eip155:1/erc721:0xee442da02f2cdcbc0140162490a068c1da94b929",
        "channel_id": "fitness"
    },
    {
        "name": "Soccer",
        "parent_url": "chain://eip155:1/erc721:0x7abfe142031532e1ad0e46f971cc0ef7cf4b98b0",
        "channel_id": "soccer"
    },
    { "name": "NFL", "parent_url": "https://www.nfl.com", "channel_id": "nfl" },
    { "name": "NBA", "parent_url": "https://www.nba.com", "channel_id": "nba" },
    {
        "name": "F1",
        "parent_url": "chain://eip155:7777777/erc721:0x47163feb5c3b97f90671b1e1a1359b8240edbdbe",
        "channel_id": "f1"
    },
    {
        "name": "Music",
        "parent_url": "chain://eip155:7777777/erc721:0xe96c21b136a477a6a97332694f0caae9fbb05634",
        "channel_id": "music"
    },
    {
        "name": "e/m",
        "parent_url": "chain://eip155:1/erc721:0x05acde54e82e7e38ec12c5b5b4b1fd1c8d32658d",
        "channel_id": "electronic"
    },
    {
        "name": "Gaming",
        "parent_url": "chain://eip155:7777777/erc721:0xa390bc5b492f4d378ca2ef513a45a89d54538f02",
        "channel_id": "gaming"
    },
    {
        "name": "Photography",
        "parent_url": "chain://eip155:7777777/erc721:0x36ef4ed7a949ee87d5d2983f634ae87e304a9ea2",
        "channel_id": "photography"
    },
    {
        "name": "Dogs",
        "parent_url": "chain://eip155:7777777/erc721:0x8cb43a65b27461b61d6c8989e6f9d88e5426833d",
        "channel_id": "dogs"
    },
    {
        "name": "Cats",
        "parent_url": "chain://eip155:7777777/erc721:0x038adac316a87c29c3acc8641e1d8320bb0144c2",
        "channel_id": "cats"
    },
    {
        "name": "Fashion",
        "parent_url": "chain://eip155:7777777/erc721:0x73a2bba481d2b4ec00ecbce45f580aabad14ae26",
        "channel_id": "fashion"
    },
    {
        "name": "Art",
        "parent_url": "chain://eip155:1/erc721:0x1538c5ddbb073638b7cd1ae41ec2d9f9a4c24a7e",
        "channel_id": "art"
    },
    {
        "name": "MangAnime",
        "parent_url": "chain://eip155:7777777/erc721:0x5a5ddb8a2d1ee3d8e9fd59785da88d573d1a84fe",
        "channel_id": "manga-anime"
    },
    {
        "name": "MJ",
        "parent_url": "https://midjourney.com",
        "channel_id": "midjourney"
    },
    {
        "name": "Space",
        "parent_url": "chain://eip155:7777777/erc721:0x31fa484c7df6e0f04f520c97a7552d72123c1bc1",
        "channel_id": "space"
    },
    {
        "name": "Backend",
        "parent_url": "chain://eip155:7777777/erc721:0x9d9f2365dc761dbcdc9af8120472c5e88c90833c",
        "channel_id": "backend"
    },
    {
        "name": "Frontend",
        "parent_url": "chain://eip155:7777777/erc721:0x3d037b11c5359fac54c3928dfad0b9512695d392",
        "channel_id": "frontend"
    },
    {
        "name": "Degen",
        "parent_url": "chain://eip155:7777777/erc721:0x5d6a07d07354f8793d1ca06280c4adf04767ad7e",
        "channel_id": "degen"
    },
    {
        "name": "Chess",
        "parent_url": "chain://eip155:7777777/erc721:0xca3e25b5c41b02ffa6f3b053426e96b59b64a9ae",
        "channel_id": "chess"
    },
    {
        "name": "Tabletop",
        "parent_url": "chain://eip155:7777777/erc721:0xf7ebaea271e84a0c40e90bc6f5889dbfa0a12366",
        "channel_id": "tabletop"
    },
    {
        "name": "History",
        "parent_url": "chain://eip155:7777777/erc721:0x177aa0bf214af03499c1fe239de20f3c4c373250",
        "channel_id": "history"
    },
    {
        "name": "Philosophy",
        "parent_url": "chain://eip155:7777777/erc721:0xc48c325f794f9105000aa27d427fbed363fa7112",
        "channel_id": "philosophy"
    },
    {
        "name": "e/acc",
        "parent_url": "chain://eip155:7777777/erc721:0xc2a1570703480b72091283decb80292c273db559",
        "channel_id": "eff-acc"
    },
    {
        "name": "Travel",
        "parent_url": "chain://eip155:7777777/erc721:0x917ef0a90d63030e6aa37d51d7e6ece440ace537",
        "channel_id": "travel"
    },
    {
        "name": "LA",
        "parent_url": "chain://eip155:1/erc721:0x750262ee8b4261e061026fc24bb640a4aa88154a",
        "channel_id": "los-angeles"
    },
    {
        "name": "NY",
        "parent_url": "chain://eip155:1/erc721:0xfdd5e7949bd72c95907c46a630d2c791f0e842c6",
        "channel_id": "new-york"
    },
    {
        "name": "SF",
        "parent_url": "chain://eip155:7777777/erc721:0x2df74b933d530c66679e6fcc4c9396ebb230ccb2",
        "channel_id": "sf"
    },
    {
        "name": "Purple",
        "parent_url": "chain://eip155:1/erc721:0xa45662638e9f3bbb7a6fecb4b17853b7ba0f3a60",
        "channel_id": "purple"
    },
    {
        "name": "Purpler",
        "parent_url": "chain://eip155:1/erc721:0x8edceb20795ac2b93ab8635af77e96cae123d045",
        "channel_id": "purpler"
    },
    {
        "name": "Builder",
        "parent_url": "chain://eip155:1/erc721:0xdf9b7d26c8fc806b1ae6273684556761ff02d422",
        "channel_id": "builder"
    },
    {
        "name": "Nouns",
        "parent_url": "chain://eip155:1/erc721:0x9c8ff314c9bc7f6e59a9d9225fb22946427edc03",
        "channel_id": "nouns"
    },
    {
        "name": "Orange",
        "parent_url": "https://www.orangedao.xyz",
        "channel_id": "orange-dao"
    },
    {
        "name": "Zorbs",
        "parent_url": "chain://eip155:1/erc721:0xca21d4228cdcc68d4e23807e5e370c07577dd152",
        "channel_id": "zorbs"
    },
    {
        "name": "Kiwi News",
        "parent_url": "chain://eip155:1/erc721:0xebb15487787cbf8ae2ffe1a6cca5a50e63003786",
        "channel_id": "kiwi-news"
    },
    {
        "name": "Launchcaster",
        "parent_url": "chain://eip155:1/erc721:0x5f4336f57cf41821522f1777321462b108de55c26",
        "channel_id": "launchcaster"
    },
    {
        "name": "Surveycaster",
        "parent_url": "chain://eip155:1/erc721:0xb58f8b1972c86aacd58f86ffae37ed31664c934d",
        "channel_id": "surveycaster"
    },
    {
        "name": "Unlonely",
        "parent_url": "chain://eip155:1/erc721:0xc7e230ce8d67b2ad116208c69d616dd6bfc96a8d",
        "channel_id": "unlonely"
    },
    {
        "name": "Events",
        "parent_url": "chain://eip155:1/erc721:0x7ea3dff0fcd9a203f594c7474f7c6bd098af0427",
        "channel_id": "event-pass"
    },
    {
        "name": "FarQuest",
        "parent_url": "chain://eip155:1/erc721:0x427b8efee2d6453bb1c59849f164c867e4b2b376",
        "channel_id": "farquest"
    },
    {
        "name": "Cabin",
        "parent_url": "https://cabin.city",
        "channel_id": "cabin-city"
    },
    {
        "name": "SBC",
        "parent_url": "https://cbr.stanford.edu/sbc23/",
        "channel_id": "sbc"
    },
    {
        "name": "ETHG NY",
        "parent_url": "https://ethglobal.com/events/newyork2023",
        "channel_id": "ethg-ny"
    },
    {
        "name": "EthCC",
        "parent_url": "chain://eip155:1/erc721:0x39d89b649ffa044383333d297e325d42d31329b2",
        "channel_id": "ethcc"
    },
    {
        "name": "FarCon",
        "parent_url": "chain://eip155:1/erc721:0x2A9EA02E4c2dcd56Ba20628Fe1bd46bAe2C62746",
        "channel_id": "farcon"
    },
    {
        "name": "Jobs",
        "parent_url": "chain://eip155:8453/erc721:0x5fcd7a54fdf08c8dbcb969bc1f021ae87affafa8"
    }
]

class FindChannelIDTool(BaseTool):
    name = "Find channel URL"
    description = '''
    Use this tool when you need to look for content in a specific channel. 
    This tool will help you find the channel URL, which you can then pass in as a parameter to the Search in channel tool.
    '''

    def _run(self, channel: str):
        lowest = {"channel_url": None, "count": 10}
        for x in channels:
            distance = Levenshtein.distance(channel.lower(), x["name"].lower())
            if distance < lowest["count"]:
                lowest["channel_url"] = x["parent_url"]
                lowest["count"] = distance

        return lowest["channel_url"]

    def _arun(self, task: Any):
        raise NotImplementedError("This tool does not support async")
