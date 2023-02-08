startNumber = 0;
counter = 2;
year = 2023;
while (counter < 10) {
    agNumber = year + '-ag-' + startNumber + counter.toString();
    counter++, startNumber++;
    console.log(agNumber)
}