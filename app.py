import fuzzer.naughty_strings as naughty_strings
import fuzzer.large_strings as large_strings
import fuzzer.naughty_numbers as naughty_numbers
import fuzzer.naughty_floats as naughty_floats

naughty_strings.send_naughty_strings_to_api(
    'root@example.com', 'Complexpass#123', 'http://localhost:5080/api/default/naughty_strings/_json')

large_strings.send_large_strings_to_api(
    'root@example.com', 'Complexpass#123', 'http://localhost:5080/api/default/large_strings/_json')

naughty_numbers.send_naughty_numbers_to_api(
    'root@example.com', 'Complexpass#123', 'http://localhost:5080/api/default/naughty_numbers/_json')

naughty_floats.send_naughty_floats_to_api(
    'root@example.com', 'Complexpass#123', 'http://localhost:5080/api/default/naughty_floats/_json')
