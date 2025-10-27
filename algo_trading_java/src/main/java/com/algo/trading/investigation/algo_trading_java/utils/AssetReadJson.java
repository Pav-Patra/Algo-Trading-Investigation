package com.algo.trading.investigation.algo_trading_java.utils;

import java.io.InputStream;


import org.springframework.core.io.ClassPathResource;
import org.springframework.stereotype.Repository;

import com.algo.trading.investigation.algo_trading_java.config.FilePaths;
import com.algo.trading.investigation.algo_trading_java.config.StaticAsset;
import com.fasterxml.jackson.databind.ObjectMapper;


@Repository
public class AssetReadJson implements AssetRepository {

    private <T> T readFromJsonClasspath(String path, Class<T> clazz) {
        ObjectMapper objectMapper = new ObjectMapper();

        try {
            InputStream inputStream = new ClassPathResource(path).getInputStream();
            return objectMapper.readValue(inputStream, clazz);
        } catch (Exception e) {
            throw new RuntimeException("Unable to read object from JSON file", e);
        }
    }

    public StaticAsset getStaticAssets() {
        return readFromJsonClasspath(FilePaths.ALL_ASSETS, StaticAsset.class);
    }

}