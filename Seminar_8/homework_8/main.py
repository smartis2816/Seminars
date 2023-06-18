import hw_task as hw


path = 'C:\\Users\\Gregory\\Desktop\\GB\\Python\\Seminars\\Seminar_8'


if __name__ == '__main__':
    data = hw.bypass_dir(path)
    hw.convert_to_json(data)
    hw.convert_to_csv(data)
    hw.convert_to_pickle(data)




