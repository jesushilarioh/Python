MIN_SALARY = 30000.0
MIN_YEARS = 2

salary = float(input('Enter your annual salary: '))

years_on_job = int(input('Enter the number of ' +
                          'years employed: '))

if salary >= MIN_SALARY:
    if years_on_job >= MIN_YEARS:
        print('You qualify for the loan.')
    else:
        print('You must have been employed',
              'for at least', MIN_YEARS,
              'years to qualify.')
else:
    print('You must earn at least $',
          format(MIN_SALARY, ',.2f'),
          ' per year to qualify.', sep='')