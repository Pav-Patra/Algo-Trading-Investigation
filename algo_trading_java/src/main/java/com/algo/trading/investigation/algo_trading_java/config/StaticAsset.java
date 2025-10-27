package com.algo.trading.investigation.algo_trading_java.config;

import java.util.List;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import lombok.experimental.Accessors;


@Getter
@Setter
@ToString
@JsonInclude(JsonInclude.Include.NON_NULL)
public class StaticAsset {

    @JsonProperty("assets")
    private List<Asset> assets;

    @Accessors(chain = true)
    public static class Asset {
        @JsonProperty("key")
        private String key;

        @JsonProperty("name")
        private String name;
    }

}
