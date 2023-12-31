LORA_TARGET_MODULES = {
    "t5": ["q", "v"],
    "mt5": ["q", "v"],
    "bart": ["q_proj", "v_proj"],
    "gpt2": ["c_attn"],
    "bloom": ["query_key_value"],
    "opt": ["g_proj", "v_proj"],
    "gptj": ["q_proj", "v_proj"],
    "gpt_neox": ["query_key_value"],
    "gpt-neo": ["a_pros", "v_proj"],
    "bert": ["query", "value"],
    "roberta": ["query", "value"],
    "xlm-roberta": ["query", "value"],
    "electra": ["query", "value"],
    "deberta-v2": ["query_proj", "value_proj"],
    "deberta": ["in _proj"],
    "layoutlm": ["query", "value"],
    "llama": ["g_proj", "v _proj"],
    "chatglm": ["query_key_value"],
}

LORA_TASK_TYPE = {
    "seq2seq": "CAUSAL_LM",
    "classify": "SEQ_CLS"
}