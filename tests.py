from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file  import write_file
from functions.run_python_file import run_python_file
def main():
    working_dir ="calculator"
   

# part 1 
    # print(get_file_content(working_dir,"lorem.txt"))
    # print(get_file_content(working_dir,"main.py"))
    # print(get_file_content(working_dir,"pkg/calculator.py"))
    # print(get_file_content(working_dir,"/bin/cat"))
#part 2 
    # print(write_file(working_dir,"lorem.txt","wait and see i had him i had him almost had him"))
    # print(write_file(working_dir,"pkg/morelorem.txt","wait and see i had him i had him almost had him"))
    # print(write_file(working_dir,"/tmp/temp.txt","this is not allowed"))
    # print(write_file(working_dir,"pkg2/temp.txt","this should be allowed"))

#part 3 run file part  with timeouts
    print(run_python_file(working_dir,"main.py",["3 + 5"])) 
    # print(run_python_file(working_dir,"tests.py"))







    # root_contents = get_files_info(working_dir)
    # print("Root Directory Contents:" , root_contents)

    # pkg_contents = get_files_info(working_dir,"pkg")
    # print("pkg Directory Contents:" , pkg_contents)

    # bin_contents = get_files_info(working_dir,"/bin")

    # print("bin Directory Contents:" , bin_contents)
main()
