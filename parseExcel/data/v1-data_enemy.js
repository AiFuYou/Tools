let data = {
	enemy_1: ["进战兵", [10, 10, 10, 0], [10, 15], 10],
	enemy_2: ["远程兵", [20, 20, 20, 10], [16, 20], 20],
	enemy_3: ["投石车", [30, 30, 30, 0], [21, 25], 30],
	enemy_4: ["超级兵", [40, 40, 40, 30], [26, 30], 40],
	enemy_5: ["人马", [50, 50, 50, 40], [31, 35], 50],
	enemy_6: ["狗头人", [60, 60, 60, 50], [36, 40], 60],
	enemy_7: ["石头人", [70, 70, 70, 0], [41, 45], 70],
	enemy_8: ["狼怪", [80, 80, 80, 0], [46, 50], 80],
	enemy_9: ["远古巨龙", [90, 90, 90, 80], [51, 55], 90],
	enemy_10: ["肉山", [100, 100, 100, 100], [56, 60], 100]
};
let dataKeys = ['enemy_name', 'attributes': ['attack', 'defense', 'hp', 'mp'], 'gold', 'exp'];
let data_enemy = {};
for (let key in data) {
	if (data.hasOwnProperty(key)) {
		let tmpData = {};
		for (let j = 0; j < dataKeys.length; ++ j) {
			tmpData[dataKeys[j]] = data[key][j];
		}
		data_enemy[key] = tmpData;
	}
}
data = null;
module.exports = data_enemy;