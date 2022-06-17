# API Documentation

### Running youThubAPI locally
- Clone repo: `git clone https://github.com/aritra1999/youtHub-api.git`
- Change directory: `cd youtHub-api`
- Create a virtual environment: `python3 -m venv venv`
- Activate virtual environment: `source venv/bin/activate`
- Install all dependencies: `pip install -r requiremtns.txt`
- Run Django server: `python manage.py runserver`

### Process Endpoint
Request URL: `http://localhost:8000/api/process/`  
Request Type: `POST`  
Request Body:  
```
{
    "type": "link",
    "link": "https://youtube.com/watch?v=9P5FA3Em1P8"
}
```
Resposnse: 
```
{
    "comments": [
        "more comments",
        "پدرسگ",
        "Fun Fact: This Video Has More Comment Than View",
        "GET THIS TO 20M COMMENT",
        "OMG",
        "aleeeeeeeeee",
        "amogus",
        "🇺🇦🇺🇦<br>remember this comment if you truly wanna know if God is Real or not. read ALL of it, and hopefully know that JESUS CRHIST is the true God. screenshot it or keep this comment somewhere to read later.<br>this should prove that Jesus is Real.<br>JESUS CHRIST will Not make you take any mark, and He will punish the tyrannical ANTI Christ. The ANTI Christ will get a terrible wound, but cure himself to reinforce his deception to decieve the non-Christians and the lukewarm Christians. (look up lukewarm Christians on Christian websites and/or the Bible.)<br>the AC will be world famous and very popular. he will make people take a mark on r hand or forhead.<br>there will be a severe punishment for not taking it. The ANTI-Christ is a control freak, the opposite of Jesus Christ. Jeus uses His power for GOOD, NOT EVIL. This is BIBLE PROPHECY. Dont trust the false god, his goal is to get people into the lake of fire. he  will go there too, despite all the FALSE MIRACLES HE WILL DO!<br>Repent of your sins to Jesus Christ before its too late, you could die today!<br>if the bigbang is real sat turns ring particles should&#39;ve moved too fast for ANY gravity.<br>And thats not even taking into account the bigbangs hot temprature which shoulda vaporized anything.<br>also there is too little antimatter in universe.<br>if bigbang is real 99.99999999999999999999999999% of our universe should Not exist because antimatter destroys matter when it make contact with matter. the bang wouldve made much of it touch matter. so we see far less stars n stuff bc the so called bigbang wouldve destroyed nearly all of it.",
        "too many top comments are songs",
        "فقط کامنت",
        "A mood of temptation takes over my mind<br>Condemned<br>Fallen weak on my knees, summon the strength<br>Of mayhem<br>I am the storm that is approaching<br>Provoking<br>Black clouds in isolation<br>I am reclaimer of my name<br>Born in flames, I have been blessed, my family crest is a demon of death<br>Forsakened, I am awakened<br>A phoenix&#39;s ashes are divine<br>Descent in misery<br>Destiny chasing time<br>Inherit the nightmare, surrounded by fate<br>Can&#39;t run away<br>Keep walking the line, between thе light<br>Led astray<br>Through vacant halls I won&#39;t surrender<br>Thе truth revealed in nights of ember<br>We fight through fire and ice forever<br>Two souls once lost and now they remember<br>I am the storm that is approaching<br>Provoking<br>Black clouds in isolation<br>I am reclaimer of my name<br>Born in flames, I have been blessed, my family crest is a demon of death<br>Forsakened, I am awakened<br>A phoenix&#39;s ashes are divine<br>Descent in misery<br>Destiny chasing time<br>Disappear into the night<br>Lost shadows left behind<br>Obsessions pulling me<br>Feeling I&#39;ve got to take what&#39;s mine<br>Beneath the shadows under veil of night<br>Constellations of blood pirouette, dancing through the grace of those who stand at my feet<br>Dreams of the black throne I keep on repeat<br>A derelict dark song from the ashes, the puppetmaster congregates all the masses<br>Pulling strings, twisting minds as blades hit<br>You want this power, then come try and take it<br>We are<br>The tree<br>Fire burns<br>Secret life<br>Bloodline yearns<br>Dark minds<br>Embrace<br>[?]<br>Bury the light deep within<br>Cast aside, there&#39;s no coming home<br>We&#39;re burning chaos in the wind<br>Drifting in the ocean all alone",
        "💯",
        "عجب بابا عجب!"
    ]
}
```
