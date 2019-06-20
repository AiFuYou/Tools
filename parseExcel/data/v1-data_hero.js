let data = [
	[1, 0, 1.0, 10, 10, 10],
	[2, 100, 1.1, 20, 20, 20],
	[3, 200, 1.2, 30, 30, 30],
	[4, 500, 1.3, 40, 40, 40],
	[5, 1000, 1.4, 50, 50, 50],
	[6, 2000, 1.5, 60, 60, 60],
	[7, 5000, 1.6, 70, 70, 70],
	[8, 10000, 1.7, 80, 80, 80],
	[9, 20000, 1.8, 90, 90, 90],
	[10, 50000, 1.9, 100, 100, 100]
];
let dataKeys = ['level', 'exp', 'exp_eff', 'attack', 'defense', 'hp'];
let hashKeys = [];
let data_hero = [];
for (let i = 0; i < data.length; ++ i) {
	let tmpData = {};
	for (let j = 0; j < dataKeys.length; ++ j) {
		tmpData[dataKeys[j]] = data[i][j];
	}
	data_hero[i] = tmpData;
}
data = null;
module.exports = data_hero;