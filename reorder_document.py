from genericpath import isdir
import os
import sys


# Add a directory witch has many different folders after script's address
def main():
    current_dir = sys.argv[1]
    if not os.path.isdir(current_dir):
        raise("passed directory is not a directory")

    folders_list = get_dirs(current_dir)
    new_list = remove_numbers(folders_list)
    change_folders_names(current_dir, folders_list, new_list)
    new_list.sort()

    for i in range(len(new_list)):
        element = new_list[i]
        address = return_address_with_number(current_dir, element, i+1)
        os.rename(os.path.join(current_dir, element), address)


def get_dirs(current_dir: str) -> list:
    output_list = []
    for item in os.listdir(current_dir):
        if os.path.isdir(os.path.join(current_dir, item)):
            output_list.append(item)

    return output_list


def remove_numbers(items: list) -> list:
    output = []
    for item in items:
        pointer = -1
        isNumber = False
        for i in range(len(item)):
            if item[i] >= "0" and item[i] <= "9":
                isNumber = True
            if isNumber and i+1 < len(item) and item[i + 1] == "-":
                pointer = i + 1
                break
            if not isNumber and i == 0:
                break
            isNumber = False

        if pointer != -1:
            item = item[pointer + 1 :]

        output.append(item)

    return output


def change_folders_names(current_dir: str, current_list: list, new_list: list) -> None:
    if len(current_list) != len(new_list):
        raise("these lists are not compatible")
    for i in range(len(current_list)):
        os.rename(os.path.join(current_dir, current_list[i]), os.path.join(current_dir, new_list[i]))


def return_address_with_number(current_dir: str, folder_name: str, count: int) -> str:
    return os.path.join(current_dir, (str(count) if count > 9 else "0" + str(count)) + "-" + folder_name)


if __name__ == "__main__":
    main()