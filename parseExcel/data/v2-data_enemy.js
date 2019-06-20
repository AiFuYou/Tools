let data = {
	enemy_1: ["进战兵", [10, 10, 10, 0, 'headIcon1'], [10, 15], 10, ['red', 'blue']],
	enemy_2: ["远程兵", [20, 20, 20, 10.5, 'headIcon1'], [16, 20], 20, ['red', 'blue']],
	enemy_3: ["投石车", [30, 30, 30, 0, 'headIcon1'], [21, 25], 30, ['red', 'blue']],
	enemy_4: ["超级兵", [40, 40, 40, 30, 'headIcon1'], [26, 30], 40, ['red', 'blue']],
	enemy_5: ["人马", [50, 50, 50, 40, 'headIcon1'], [31, 35], 50, ['red', 'blue']],
	enemy_6: ["狗头人", [60, 60, 60, 50, 'headIcon1'], [36, 40], 60, ['red', 'blue']],
	enemy_7: ["石头人", [70, 70, 70, 0, 'headIcon1'], [41, 45], 70, ['red', 'blue']],
	enemy_8: ["狼怪", [80, 80, 80, 0, 'headIcon1'], [46, 50], 80, ['red', 'blue']],
	enemy_9: ["远古巨龙", [90, 90, 90, 80, 'headIcon1'], [51, 55], 90, ['red', 'blue']],
	enemy_10: ["肉山", [100, 100, 100, 100.7, 'headIcon1'], [56, 60], 100, ['red', 'blue']]
};
let dataKeys = ['enemy_name', ['attack', 'defense', 'hp', 'mp', 'headIcon'], 'gold', 'exp', ['scene1', 'scene2']];
let hashKeys = ['attributes', 'color'];

let data_enemy = {};
data_enemy.dataKeys = dataKeys;
data_enemy.hashKeys = hashKeys;
data_enemy.data = data;
module.exports = data_enemy;