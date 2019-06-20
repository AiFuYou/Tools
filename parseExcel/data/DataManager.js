let DataManager = module.exports = {};
let DataEnemy = require('v2-data_enemy');
let DataHero = require('v2-data_hero');

DataManager.getHeroDataByLvl = function (lvl) {
    return this.structureData(DataHero.data[lvl - 1], DataHero.dataKeys, DataHero.hashKeys);
};

DataManager.getEnemyDataByID = function (enemyID) {
    return this.structureData(DataEnemy.data[enemyID], DataEnemy.dataKeys, DataEnemy.hashKeys);
};

DataManager.structureData = function (data, dataKeys, hashKeys) {
    let tmpData = {};
    let hashKeyIndex = 0;
    for (let i = 0; i < dataKeys.length; ++ i) {
        if (typeof dataKeys[i] === 'object') {
            let curKey = hashKeys[hashKeyIndex];
            tmpData[curKey] = {};
            for (let j = 0; j < dataKeys[i].length; ++ j) {
                tmpData[curKey][dataKeys[i][j]] = data[i][j];
            }
            ++ hashKeyIndex;
        } else {
            tmpData[dataKeys[i]] = data[i];
        }
    }
    return tmpData;
};