import random
import name_generator
import math


execute_info = {
    "guillotine": {"desc": "The guillotine was an execution method frequently used as a way to execute people for crimes during the French Revolution. The Guillotine was known to have killed 40,000 people during the French Revolution. The guillotine was an official method of execution up until 1981 in France, the last person ever executed by the guillotine was in 1977. The first guillotine was made in 1791.\n\nLinks:\nhttps://ageofrevolution.org/200-object/a-french-guillotine-blade/#:~:text=The%20guillotine%20is%20best%20known,guillotine%20was%20quick%20and%20humane.", "asupport": 70, "acontroversy": 65, "amorality": 75},
    "firing_squad": {"desc": "The firing squad was when 5 or more people would line up beside each other and take aim at the person's heart, the person being shot would be blindfolded. The people would wait for a signal from the senior officer they would fire. The shots fired would hit the heart and the person getting shot to die by his wound and blood loss/rupture in his heart. This method was frequently used against soldiers who had performed traitorous acts/not participating in the war effort.\n\nLinks:\nhttps://www.crimemuseum.org/crime-library/execution/firing-squad/#:~:text=Five%20or%20more%20soldiers%20line,placed%20before%20the%20firing%20squad.\nhttps://www.npr.org/2023/03/26/1166139433/idaho-is-the-latest-state-to-permit-execution-by-firing-squad#:~:text=Mississippi%2C%20Oklahoma%2C%20Utah%20and%20South%20Carolina%20also%20permit%20the%20method,a%20Utah%20prison%20in%202010.", "asupport": 65, "acontroversy": 40, "amorality": 85},
    "hanging": {"desc": "Hanging was a very commonly used method of execution during the French Revolution. Hanging would happen in 2 ways either a person would climb up a ladder or a newer version of the trapdoor. The hanging method was not the most effective execution because it did not always kill the person right away. The point of hanging would be that the criminal would break their neck, but this was not always the outcome, Sometimes the criminal wouldn’t break their neck and they would just strangle to death. The last public hanging took place in Britain in 1868.\n\nLinks:\nhttps://websites.umich.edu/~ece/student_projects/gallows/Top%2010%20Punishments.html", "asupport": 80, "acontroversy": 45, "amorality": 60},
    "private": {"desc": "Public executions were filled with drama, gossip, and excitement for entertainment, and they normally had people being obnoxious, disturbing, and rowdy. This is why private executions because another execution method. This would ensure that the execution was done well and professionally. Another reason for this is that Queen Anne Boleyn was beheaded in a private execution. They held a private execution because a Queen being beheaded in public would show the rulership and power of the monarch in a bad light.", "asupport": 35, "acontroversy": 85, "amorality": 70},
    "imprison": {"desc": "Freedom was given to convicted criminals when they were either found not guilty of a crime or the support of the person was so high that their execution would cause outrage in the community. Although this option was very uncommon.", "asupport": 40, "acontroversy": 70, "amorality": 40},
    "freedom": {"desc": "Imprisonment was given to people who had committed small crimes that didn't fit the executions. The small crimes included small thefts and vandalism. These people instead of being given the death penalty they were given time in prison.", "asupport": 10, "acontroversy": 10, "amorality": 10}
}

execute_sit = {
    "support":[#High value represents wanted death
        {"val":5,"text":" People are rallying for the freedom of /*name/"},
        {"val":10,"text":" Many people are gathering to support /*name/'s freedom"},
        #{"val":20,"text":"s20"},
        #{"val":30,"text":"s30"},
        {"val":40,"text":" Only a small amount of the general public has voiced opinion, but those who do are in support of /*name/'s freedom"},
        {"val":50,"text":" Very few people from the general population have said their opinions, but they are hoping for a successful execution of /*name/"},
        #{"val":60,"text":"s60"},
        #{"val":70,"text":"s70"},
        {"val":80,"text":" Many are hoping and fighting for the death of /*name/"},
        {"val":90,"text":" A majority of people are petitioning for /*name/ to be executed"},
        ],
    "controversy":[#High value represents large divide
        {"val":5,"text":", and not a single word or voice of opinion has been heard defending the opposite"},
        {"val":10,"text":", and only small, quiet groups have extreme opinions on the execution"},
        {"val":20,"text":", and some small groups have been attempting to sway general opinion."},
        {"val":30,"text":", but some bigger groups are quietly working for the opposing side."},
        {"val":40,"text":", but multiple large groups are portraying the opposite to be the obvious choice"},
        {"val":50,"text":"but, a few bigger groups are loudly proclaiming that /*name/ should have a different outcome"},
        {"val":60,"text":"but, some groups of fanatics have been protesting against this."},
        {"val":70,"text":"but, there are a few large groups that are rallying for the opposite."},
        {"val":80,"text":", however, many groups are loudly proclaiming there opinions in an attempt to sway the general public."},
        {"val":90,"text":", however, large groups exist that are loudly voicing their opinion on the matter."},
        ],
    "morality":[#High value represents terrible crimes
        {"val":5,"text":"/*name/ has been detained for stepping on a flower bed while on a walk one morning. /*name/ stumbled and fell onto the flowers of a nobleman, and is now being charged with destruction of property."},
        {"val":10,"text":"/*name/, in a drunken stupor, broke multiple chairs and glasses at a local tavern. Whilst in this rage, /*name/ threatened multiple patrons and attempted to start a fight. Soon after, /*name/ was taken into custody"},
        #{"val":20,"text":"m20"},
        #{"val":30,"text":"m30"},
        {"val":40,"text":"/*name/ attempted to commit arson after hearing a speach given by a government official. Before /*name/ was able to, the police saw and detained /*name/."},
        {"val":50,"text":"/*name/ has been found to have been spreading rumors and lies about the countries king. /*name/ has also be paying the press to take his opinions and publish them as fact."},
        {"val":60,"text":"/*name/ was cought stealing precious gems and minerals from multiple stores in the city. /*name/, however, has not been solidly proven, nor has admitted to these crimes"},
        {"val":70,"text":"/*name/ has been masquerading as a doctor, selling poison as remedys causing a large number of possible deaths. /*name/ has just recently been aprehended and has confessed to the crime."},
        {"val":80,"text":"/*name/ has commited murder. /*name/ has been found, and proven, guilty for the murder of a family of 4. No evidence has been released to the public yet, but word has gotten out for why /*name/ is being executed."},
        {"val":90,"text":"/*name/ has attempted to commit genocide. /*name/ had fashioned make-shift explosives and planted them within a large population center. Little to no evidence exists to prove /*name/ guilty that has been shown to the public."},
        ]
}
#vales of 0-100

def sit_former():
    chosen_first_name = random.choice(name_generator.first_names)
    chosen_last_name = random.choice(name_generator.last_names)

    chosen_s = random.choice(execute_sit["support"])
    chosen_c = random.choice(execute_sit["controversy"])
    chosen_m = random.choice(execute_sit["morality"])


    formed_text = "Situation:\n\n"
    formed_text += chosen_m["text"]
    formed_text += chosen_s["text"]

    formed_text += chosen_c["text"]


    formed_text = formed_text.split("/")
    name_introduced = False

    for section_num, section_val in enumerate(formed_text):
        if section_val == "*name":
            if not name_introduced:
                formed_text[section_num] = (chosen_first_name + " " + chosen_last_name)
                name_introduced = True
            else:
                formed_text[section_num] = chosen_first_name
    
    formed_text = "".join(formed_text)

    formed_text = formed_text.split(" ")

    for word_num, _ in enumerate(formed_text):
        if word_num%12 == 0:
            formed_text.insert(word_num, "\n")
        
    formed_text = " ".join(formed_text)



    return {"text":formed_text,"support":chosen_s["val"],"controversy":chosen_c["val"],"morality":chosen_m["val"]}

def get_deviation(situation, exe_method):
    div_s = abs(int(situation["support"]) - int((execute_info[exe_method])["asupport"]))
    div_c = abs(int(situation["controversy"]) - int((execute_info[exe_method])["acontroversy"]))
    div_m = abs(int(situation["morality"]) - int((execute_info[exe_method])["amorality"]))
    return (div_s+div_c+div_m)/3

def interaction_menu():
    questions_asked = 0
    total_score = 0
    while True:
        for _ in range(0,100):
            print("\n")

        print(f"Current Score: ({total_score}/{questions_asked})")
        questions_asked += 1

        random_situation = sit_former()
        exe_type_scores = {"g":get_deviation(random_situation, "guillotine"),
                           "fs":get_deviation(random_situation, "firing_squad"),
                           "h":get_deviation(random_situation, "hanging"),
                           "p":get_deviation(random_situation, "private"),
                           "i":get_deviation(random_situation, "imprison"),
                           "fd":get_deviation(random_situation, "freedom")
                        }
        exe_scores_final = {}

        i_count = 0
        for exe_val in sorted(exe_type_scores.items(), key=lambda x:x[1]):
            exe_scoring_pos = 0
            if i_count in [0,1]:
                exe_scoring_pos = 1
            elif i_count in [2,3]:
                exe_scoring_pos = 0.5

            exe_scores_final.update({list(exe_val)[0]:exe_scoring_pos})
            i_count += 1


        print(random_situation["text"])
        print("\n1:Guillotine\n2:Firing Squad\n3:Hanging\n4:Private Execution\n5:Imprisonment\n6:Freedom")
        skipped_question = False
        while True:
            
            user_choice = input("\nChoose an option.\n(type \"!help\" for a list of options)\n>: ").lower()

            if user_choice in ["!help"]:
                print("Help requested")
                print("COMMANDS:")
                print("    # - Choice of execution method")
                print("    info # - Get info on execution method")
            elif user_choice in ["!skip"]:
                questions_asked -= 1
                skipped_question = True
                break
            elif user_choice in ["!debug"]:
                print(f"Morality: {random_situation['morality']}")
                print(f"Support: {random_situation['support']}")
                print(f"Controversy: {random_situation['controversy']}")

                print(exe_scores_final)

                for val_key, val in exe_type_scores.items():
                    print(val_key)
                    print(val)
            elif user_choice in ["1","2","3","4","5","6"]:
                print(list(execute_info.keys())[int(user_choice)-1])
                print(f"You got {exe_scores_final[list(exe_type_scores.keys())[int(user_choice)-1]]} points!")
                total_score += exe_scores_final[list(exe_type_scores.keys())[int(user_choice)-1]]
            
                break

            elif user_choice in ["info 1","info 2","info 3","info 4","info 5", "info 6"]:
                chosen_exe = int(user_choice.split(" ")[-1])-1

                if chosen_exe not in [1,3,4]:
                    print(f"{list(execute_info.keys())[chosen_exe].capitalize()} info:")
                elif chosen_exe == 1:
                    print("Firing squad info:")
                elif chosen_exe == 3:
                    print("Private execution info:")
                else:
                    print("Imprisonment info:")
                exe_info_text = list(execute_info.values())[chosen_exe]["desc"]
                exe_info_text = exe_info_text.split(" ")

                exe_final_text = ""
                for count,val in enumerate(exe_info_text):
                    exe_final_text += val
                    exe_final_text += " "
                    if (count%15 == 0) and (count >= 15):
                        exe_final_text += "\n"
                print(exe_final_text)
            
        if skipped_question:
            continue

interaction_menu()
