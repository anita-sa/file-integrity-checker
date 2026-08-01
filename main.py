import argparse
import os

from hasher import calculate_hash, get_files
from database import save_hash, get_hash




def scan(path):

    try:

        files = get_files(path)


        if not files:

            print("\n❌ No files found")
            return


        count = 0


        print("\nScanning...\n")


        for file in files:

            file_hash = calculate_hash(file)

            save_hash(file, file_hash)

            print("✔", file)

            count += 1



        print(
            f"\n{count} files saved"
        )


    except FileNotFoundError:

        print("\n❌ Path not found:")
        print(path)



def check(path):

    try:

        if not os.path.exists(path):

            print("\n❌ Path not found:")
            print(path)
            return


        files = get_files(path)


        if not files:

            print("\n❌ No files found")
            return


        print("\nChecking integrity...\n")


        for file in files:

            saved_hash = get_hash(file)


            if saved_hash is None:

                print("❌ Not registered:", file)
                continue


            current_hash = calculate_hash(file)


            if saved_hash == current_hash:

                print("✔", file)


            else:

                print("⚠ Modified:", file)



    except FileNotFoundError:

        print("\n❌ File not found:")
        print(path)



def main():

    parser = argparse.ArgumentParser(
        description="File Integrity Checker - SHA256 based monitoring tool"
    )


    subparsers = parser.add_subparsers(
        dest="command"
    )


    # scan command
    scan_parser = subparsers.add_parser(
        "scan",
        help="Save file hash"
    )

    scan_parser.add_argument(
        "file",
        help="File path to scan"
    )


    # check command
    check_parser = subparsers.add_parser(
        "check",
        help="Check file integrity"
    )

    check_parser.add_argument(
        "file",
        help="File path to check"
    )



    args = parser.parse_args()



    if args.command == "scan":

        scan(args.file)



    elif args.command == "check":

        check(args.file)



    else:

        parser.print_help()



if __name__ == "__main__":
    main()