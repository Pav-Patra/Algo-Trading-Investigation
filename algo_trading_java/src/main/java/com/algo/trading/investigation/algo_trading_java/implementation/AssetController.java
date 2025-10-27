package com.algo.trading.investigation.algo_trading_java.implementation;

import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import com.algo.trading.investigation.algo_trading_java.config.Asset;
import com.algo.trading.investigation.algo_trading_java.config.StaticAsset;
import com.algo.trading.investigation.algo_trading_java.utils.AssetRepository;

@RestController
public class AssetController {

    AssetRepository assetRepository;

    public AssetController(AssetRepository assetRepository) {
        this.assetRepository = assetRepository;
    }

    @GetMapping(path="/assets")
    public List<StaticAsset.Asset> getAssets() {
        return assetRepository.getStaticAssets().getAssets();
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
