import data_csv
import population
import charts

def run():
    data = data_csv.information_from_csv('./information_data.csv')
    country = input('Type a Country => ')

    result = population.population_by_country(data,country)
    
    if len(result)>0:
        country = result[0]
        keys, values = population.get_population(country)
        charts.generate_bar_chart(keys,values)



if __name__ == '__main__':
    run()