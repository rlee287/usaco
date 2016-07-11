import os
import sys

if __name__=="__main__":
    print(sys.argv)
    if "--clean" in sys.argv:
        n=1
        while True:
            try:
                os.remove(sys.argv[1]+".out."+str(n))
            except FileNotFoundError:
                break
            n+=1
    else:
        target_name=sys.argv[1]
        target_name_in=target_name+".in"
        target_name_out=target_name+".out"
        file_run=sys.argv[2]
        n=1
        while True:
            orig_name="{}.in".format(n)
            if os.path.isfile(orig_name):
                print("Renaming",orig_name,"to",target_name_in)
                os.rename(orig_name,target_name_in)
                print("Executing",file_run)
                with open(file_run, "r") as file_handle:
                    exec(file_handle.read())
                print("Renaming",target_name_in,"to",orig_name)
                os.rename(target_name_in,orig_name)
                target_name_out_n=target_name_out+"."+str(n)
                print("Renaming",target_name_out,"to",target_name_out_n)
                os.rename(target_name_out,target_name_out_n)
                with open("{}.out".format(n)) as correct_file:
                    correct=correct_file.read()
                with open(target_name_out_n) as produced_file:
                    produced=produced_file.read()
                print("  Correct is",correct)
                print("  Produced is",produced)
                print("  Correct" if correct==produced else "  Incorrect")
            else:
                break
            n+=1
