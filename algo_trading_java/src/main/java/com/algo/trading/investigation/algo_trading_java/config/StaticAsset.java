package com.algo.trading.investigation.algo_trading_java.config;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;


@Getter
@Setter
@ToString
@JsonInclude(JsonInclude.Include.NON_NULL)
public class StaticAsset {

    @JsonProperty("key")
    private String key;

    @JsonProperty("name")
    private String name;

}
