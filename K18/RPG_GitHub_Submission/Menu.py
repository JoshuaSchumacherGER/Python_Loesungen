import sys
sys.path.insert(0,'/home/dev/Git/Project--RPG-Fighting-Game/playerclasses')
#Game Menu
while True:
    print(''' Choose:
    Fight
    Journey
    Reload Assets''')

    pregamevar = input()


    if pregamevar in ("Fight"):
        import fight
        fight.game()
        break
        #print"("Shut down for maintenance")
    elif pregamevar in ("Journey"):
        #import journey
        #journey.game()
        #break
        print("Shut down for maintenance")
    elif pregamevar == "Reload Assets":
        import reload_assets
        reload_assets.save()
        print("Assets updated successfullly")
        #print("Shut down for maintenance")
    else:
        print("Not an option")