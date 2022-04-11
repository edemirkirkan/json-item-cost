# json-item-cost

Given the json structure of an item either  {"name": str, "count": int, "items": []} or {"name": str, "count": int, "price": int}, the program can calculate the total cost of the any item combinations.

<ins>Sample Input</ins><br>
```
{
	"name": "a",
	"count": 2,
	"items": [
		{
			"name": "x",
			"count": 1,
			"items": [
				{
					"name": "x_1",
					"count": 5,
					"price": 1
				},
				{
					"name": "x_2",
					"count": 2,
					"items": [
						{
							"name": "x_2_1",
							"count": 1,
							"price": 10
						},
						{
							"name": "x_2_2",
							"count": 2,
							"price": 24
						}
					]
				},
				{
					"name": "x_3",
					"count": 3,
					"price": 2
				}
			]
		},
		{
			"name": "y",
			"count": 2,
			"price": 2
		},
		{
			"name": "z",
			"count": 3,
			"price": 3
		}
	]
}
```
<ins>Sample Output</ins><br>
280 



