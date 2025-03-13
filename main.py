import sys, getopt
from scraper import crawler

if __name__ == "__main__":
    query = ""
    scroll = 2
    folder_name = ""
    size = 0

    if len(sys.argv) == 1:
        print("main.py -q <query> -s <scroll> -f <folder_name>")
        sys.exit(2)

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hq:s:f:z", ["query=", "scroll=", "folder_name=", "size="])
    except getopt.GetoptError:
        print("main.py -q <query> -s <scroll> -f <folder_name>")
        sys.exit(2)
        
    for opt, arg in opts:
        if opt == "-h":
            print("main.py -q <query> -s <scroll> -f <folder_name> -z <size>")
            sys.exit()
        elif opt in ("-q", "--query"):
            # replace white space with '+'
            query = arg.replace(" ", "+")
        elif opt in ("-s", "--scroll"):
            scroll = int(arg)
        elif opt in ("-f", "--folder_name"):
            folder_name = arg
        elif opt in ("-z", "--size"):
            size = int(arg)
    
    print(f"query: {query}, scroll: {scroll}, folder_name: {folder_name}")
    crawler(query, scroll, folder_name)