package io.agilehandy.graalpy;

import org.graalvm.polyglot.Value;

public interface Watsonx {

    Object setWatsonxModel(String model, String apiKey, String projectId) ;

    String invoke(String promot);

}
