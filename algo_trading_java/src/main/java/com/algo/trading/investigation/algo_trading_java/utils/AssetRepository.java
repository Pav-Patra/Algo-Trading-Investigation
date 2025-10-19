package com.algo.trading.investigation.algo_trading_java.utils;

import java.util.List;

import com.algo.trading.investigation.algo_trading_java.config.StaticAsset;

public interface AssetRepository {

    public List<StaticAsset> getAssetsList();
    
}
