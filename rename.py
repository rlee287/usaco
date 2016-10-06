import os
import sys

if __name__=="__main__":
    if "-i" in sys.argv:
        target_name=input("Please enter the target name the program will read: ")
        file_run=input("Please enter the name of the program file: ")
    else:
        target_name=sys.argv[1]
        file_run=sys.argv[2]
    target_name.rstrip(".in")
    target_name.rstrip(".out")
    if "--clean" in sys.argv:
        n=1
        while True:
            try:
                os.remove(target_name+".out."+str(n))
            except FileNotFoundError:
                break
            n+=1
    else:
        target_name_in=target_name+".in"
        target_name_out=target_name+".out"
        correct_list=list()
        n=1
        while True:
            orig_name="{}.in".format(n)
            if os.path.isfile(orig_name):
                print("Renaming",orig_name,"to",target_name_in)
                os.rename(orig_name,target_name_in)
                print("Executing",file_run)
                os.system("python "+file_run)
                print("Renaming",target_name_in,"to",orig_name)
                os.rename(target_name_in,orig_name)
                target_name_out_n=target_name_out+"."+str(n)
                print("Renaming",target_name_out,"to",target_name_out_n)
                os.rename(target_name_out,target_name_out_n)
                with open("{}.out".format(n)) as correct_file:
                    correct=correct_file.read()
                with open(target_name_out_n) as produced_file:
                    produced=produced_file.read()
                correct=correct.rstrip("\n")
                produced=produced.rstrip("\n")
                print("  Correct is",correct)
                print("  Produced is",produced)
                correct_bool=(correct==produced)
                correct_list.append(correct_bool)
                print("  Correct" if correct_bool else "  Incorrect")
                n+=1
            else:
                total_correct=0
                total_incorrect=n
                for num,corr in enumerate(correct_list):
                    print(num+1,corr)
                    if corr:
                        total_correct+=1
                        total_incorrect-=1
                print("-------- {0} correct, {1} incorrect --------"
                      .format(total_correct,total_incorrect))
                break
