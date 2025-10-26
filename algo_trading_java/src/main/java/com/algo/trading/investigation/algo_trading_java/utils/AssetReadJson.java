package com.algo.trading.investigation.algo_trading_java.utils;

import java.io.File;

import com.algo.trading.investigation.algo_trading_java.config.FilePaths;
import com.algo.trading.investigation.algo_trading_java.config.StaticAsset;
import com.fasterxml.jackson.databind.ObjectMapper;



public class AssetReadJson implements AssetRepository {

    private <T> T readFromJson(String path, Class<T> clazz) {
        ObjectMapper objectMapper = new ObjectMapper();
        try {
            return objectMapper.readValue(new File(path), clazz);
        } catch (Exception e) {
            throw new RuntimeException("Unable to read object from JSON file", e);
        }
    }

    public StaticAsset getAssets() {
        return readFromJson(FilePaths.ALL_ASSETS, StaticAsset.class);
    }

}
