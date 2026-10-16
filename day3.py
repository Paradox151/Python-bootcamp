print('''  ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--` ''')

print("welcome to tresure island your mission is to find the treasure")
d1= input("there are two tunnels where you would like to turn left or right?:").lower()
if d1== "left":
    d2 = input('''right choice you passed theres a monster sleeping with a" \
    "diamond ring handing in his sword 
               
                                              ,--,  ,.-.
                ,                   \,       '-,-`,'-.' | ._
               /|           \    ,   |\         }  )/  / `-,',
               [ '          |\  /|   | |        /  \|  |/`  ,`
               | |       ,.`  `,` `, | |  _,...(   (      _',
   -ART BY-    \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L"\"
    -ZEUS-      \  \_\,``,   ` , ,  /  |         )         _,/
                 \  '  `  ,_ _`_,-,<._.<        /         /
                  ', `>.,`  `  `   ,., |_      |         /
                    \/`  `,   `   ,`  | /__,.-`    _,   `"\"
                -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                 \_,,.) /\    ` /  / ) (-,, ``    ,        |
                ,` )  | \_\       '-`  |  `(               \
               /  /```(   , --, ,' \   |`<`    ,            |
              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
       (-, \           ) \ ('_.-._)/ /,`    /
       | /  `          `/ \\ V   V, /`     /
    ,--\(        ,     <_/`\\     ||      /
   (   ,``-     \/|         \-A.A-`|     /
  ,>,_ )_,..(    )\          -,,_-`  _--`
 (_ \|`   _,/_  /  \_            ,--`
  \( `   <.,../`     `-.._   _,-`
   `                      ```
would you like to "take" or "run" away from him:?''')
    if d2 == "run":
        d3 = input("wise choice never disturb a sleeping beast you passed " \
        "there is a secret room of thet beast with some mistry box " \
        "would you like to go \"closer\" or \"slide\" through the secret passage:? ")
        if d3== "slide":
            d4 = input("fair choice that was a trap you went out to the shore " \
            "there is a island with the x mark would you like to 'swim' or ' wait' for your" \
            "crewmate to appear")
            if d4 == "wait":
                print('''congratulation you won the game the tresure\'s your \
                "
         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|''')
            else:
                print("failed monster pet piranas eat you")
        else:
            print("failed that was a trap monster capyur you and took out you eyes")
            
    else:
        print("failed the monster wokeup and make a dinner of you")
else: 
    print("you fall into abyss misson failed")
