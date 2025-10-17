package com.algo.trading.investigation.algo_trading_java.implementation;

import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import com.algo.trading.investigation.algo_trading_java.config.Asset;

@RestController
public class AssetController {

    @GetMapping(path="/assets")
    public List<Asset> getAssets() {
        return null;
    }

    @GetMapping(path="/asset/{id}")
    public Asset getAsset(@PathVariable("id") String assetId) {
        return null;
    }

    @GetMapping(path="/percentChange/{id}/{mins}")
    public float getAssetPriceChange(@PathVariable("id") String assetId, @PathVariable("mins") int minutes) {
        return 0;
    }

    @GetMapping(path="/percentChange/{mins}")
    public float getAllPriceChange(@PathVariable("mins") int minutes) {
        return 0;
    }
}
