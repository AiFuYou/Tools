let data = {
	enemy_1: ["进战兵", {attack: 10, defense: 10, hp: 10, mp: 0}, [10, 15], 10],
	enemy_2: ["远程兵", {attack: 20, defense: 20, hp: 20, mp: 10}, [16, 20], 20],
	enemy_3: ["投石车", {attack: 30, defense: 30, hp: 30, mp: 0}, [21, 25], 30],
	enemy_4: ["超级兵", {attack: 40, defense: 40, hp: 40, mp: 30}, [26, 30], 40],
	enemy_5: ["人马", {attack: 50, defense: 50, hp: 50, mp: 40}, [31, 35], 50],
	enemy_6: ["狗头人", {attack: 60, defense: 60, hp: 60, mp: 50}, [36, 40], 60],
	enemy_7: ["石头人", {attack: 70, defense: 70, hp: 70, mp: 0}, [41, 45], 70],
	enemy_8: ["狼怪", {attack: 80, defense: 80, hp: 80, mp: 0}, [46, 50], 80],
	enemy_9: ["远古巨龙", {attack: 90, defense: 90, hp: 90, mp: 80}, [51, 55], 90],
	enemy_10: ["肉山", {attack: 100, defense: 100, hp: 100, mp: 100}, [56, 60], 100]
};
let dataKeys = ['enemy_name', 'attributes', 'gold', 'exp'];
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