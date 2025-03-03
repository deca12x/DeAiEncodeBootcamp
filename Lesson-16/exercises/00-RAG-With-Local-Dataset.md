# Using RAG with Local Dataset in the Text Generation WebUI

1. Setup the `superbooga` extension in Text Generation Web UI
   - Restart the Text Generation Web UI and activate the `superbooga` extension
     - Activate [Superbooga](https://github.com/oobabooga/text-generation-webui/tree/main/extensions/superbooga) in the `Session` tab
   - Click on `Apply flags/extensions and restart` to load the extension
   - Stop the Web UI by pressing `Ctrl+C`/`Cmd+C` in the terminal
   - Run the `update_wizard_<your OS>` script
     - Pick the `B) Install/update extensions requirements` option
     - Then pick the `F) superbooga` option
     - Wait for the install to finish
     - Exit the script
2. Select a model in the `Model` tab
   - Choose a suitable model that is trained for instruction-following tasks
     - For example using `Vicuna 7B v1.5` model in the [GGUF](https://huggingface.co/TheBloke/vicuna-7B-v1.5-GGUF) or [AWQ version](https://huggingface.co/TheBloke/vicuna-7B-v1.5-AWQ)
3. Open the `Notebook` tab
4. Input the following prompt into the `Textbox`:

   ```text
   USER:
   <|begin-user-input|>
   What is this recipe about?
   <|end-user-input|>

   <|injection-point|>

   ASSISTANT:
   ```

5. Click `Generate` to produce the response
   - The `<|injection-point|>` will be empty, since we haven't loaded any data yet
   - The generated response should be a generic hallucination from the model or something similar
6. Scroll down to see the `File input` tab and upload the [Sample Data](../examples/SampleText.txt) there
   - Configure `\n` as the `Chunk separator` to split the file into paragraphs
7. Click on `Load data` to add the _chunks_ to the database
8. Test the prompt once more
   - The response should now contain information from the Sample Data
   - Each chunk in the database will be compared to the current input, and the most relevant matches will be appended to the input before starting the inference process
     - You can configure the amount of context to be appended by changing the `Chunk count` value in the `Generation settings` tab
       - For example, you can set it to `1` to append only the single most relevant chunk pertaining to the current input
9. You may also test the RAG functionalities in the `Chat` tab
   - This only works in the `instruct` mode
   - In the `chat` mode, the extension maintains an extended context with the conversation history
     - At each new message, the most relevant past messages will be appended to the context string, and the extension will ignore the external data sources
