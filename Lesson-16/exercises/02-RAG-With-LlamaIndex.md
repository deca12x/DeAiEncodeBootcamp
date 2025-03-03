# Building a RAG Pipeline with LlamaIndex

1. Clone the [LlamaIndex TypeScript Playground](https://github.com/run-llama/ts-playground)

   ```bash
   git clone https://github.com/run-llama/ts-playground.git
   cd ts-playground
   ```

2. Install the dependencies

   ```bash
   npm install
   ```

3. Run the project

   ```bash
   npm run dev
   ```

4. Open the application in your browser and test the RAG features

   - Navigate to <http://localhost:3000>
   - Use the default settings and suggested text
   - Click on `Build Index`
     - The button should change to `Building Vector index...`
   - Wait for the embeddings to be created
     - This step may take several minutes
   - After the embeddings are created, input a query in the `Query` field
     - For example: `What happened in the end of 2015?`
       - The answer should be similar to this: `The author joined the React Core team as the only UK member.`

5. Open the project in your code editor

   ```bash
   code .
   ```

6. Open the `index.tsx` file in the `pages` folder

   - Locate the `textarea` element inside the `main` div

7. Replace the code of the `textarea` with a `file input`

   - Set the accept attribute to `.txt` to allow only text files
     - Parsing other file types is more complex and would require additional libraries

   ```tsx
   <div className="my-2 flex h-3/4 flex-auto flex-col space-y-2">
     <Label htmlFor={sourceId}>Upload source text file:</Label>
     <Input
       id={sourceId}
       type="file"
       accept=".txt"
       onChange={(e: ChangeEvent<HTMLInputElement>) => {
         // File handling logic will be added here
       }}
     />
   </div>
   ```

8. Implement file reading logic

   ```tsx
      onChange={(e: ChangeEvent<HTMLInputElement>) => {
     const file = e.target.files?.[0];
     if (file) {
       const reader = new FileReader();
       reader.onload = (event) => {
         const fileContent = event.target?.result as string;
         setText(fileContent);
         setNeedsNewIndex(true);
       };
       if (file.type != "text/plain") {
         console.error(`${file.type} parsing not implemented`);
         setText("Error");
       } else {
         reader.readAsText(file);
       }
     }
   }}
   ```

9. Change the `label` for `Source text:`

   ```tsx
   <Label htmlFor={sourceId}>Upload source text file:</Label>
   ```

10. Add a display area for the uploaded text after the `file input`

    ```tsx
    {
      text && (
        <Textarea
          value={text}
          readOnly
          placeholder="File contents will appear here"
          className="flex-1"
        />
      );
    }
    ```

11. Save the changes and test the application again

12. Load the [Shrek.txt](../examples/Shrek.txt) file in the input field

13. Select the maximum value for the `Chunk size` slider (`3000`) and click on `Build Index`

    - The bigger the chunk size, the faster the index is created, but the less accurate the results will be

14. After the process is complete, input a query in the `Query` field

    - For example: `List the name, description, and personality of every character`

      - The answer should be similar to this:

        ```text
        1. Shrek: Shrek is an ogre who lives in a swamp. He values his privacy and is initially portrayed as grumpy and intimidating, but also has a sarcastic sense of humor. He is also brave and willing to stand up to those who threaten him or his home. He is determined to reclaim his swamp from the fairy tale creatures who have been forced to take refuge there.

        2. Donkey: Donkey is a talking donkey who is very chatty and outgoing. He is also quite persistent and tends to not take hints easily. Despite his sometimes annoying behavior, he is friendly and means well. He is also adventurous, as he is excited about the idea of going on a "whirlwind big-city adventure" with Shrek.

        3. Man1, Man2, Man3: These are villagers who are initially scared of Shrek and believe him to be dangerous. They are easily frightened and not very brave.

        4. The Head Guard: The Head Guard is in charge of collecting fairy tale creatures. He is authoritative and strict, showing little sympathy for the creatures he is rounding up.

        5. Gipetto: Gipetto is the creator of Pinocchio. He is shown to be willing to sell Pinocchio for money, suggesting he may be desperate or unkind.

        6. Pinocchio: Pinocchio is a wooden puppet who insists he is a real boy. He is upset when Gipetto sells him, showing he has feelings and desires of his own.

        7. The Old Woman: The Old Woman tries to sell Donkey, showing she can be deceitful. She is also desperate, as she tries to prove Donkey can talk to avoid being taken away by the guards.

        8. The Three Little Pigs: The Three Little Pigs are among the fairy tale creatures being rounded up. They don't have much dialogue, so their personalities aren't clear.

        9. The Big Bad Wolf: The Big Bad Wolf is found in Shrek's bed. He doesn't say much, so his personality isn't clear.

        10. Lord Farquaad: Lord Farquaad is the ruler of Duloc who has forced the fairy tale creatures to leave their homes, suggesting he is powerful and possibly cruel. He is also shown to be short in stature, which he compensates for with a very tall castle. He is determined to become a king by marrying a princess. He is also ruthless, as shown by his treatment of the Gingerbread Man.

        11. Gingerbread Man: The Gingerbread Man is a fairy tale creature who is being tortured by Lord Farquaad for information. He is defiant and refuses to give up his friends, showing he is brave and loyal.

        12. Magic Mirror: The Magic Mirror is a magical object that provides information and advice. It is forced to help Lord Farquaad in his quest to become a king.

        13. Thelonius: Thelonius is a henchman of Lord Farquaad. He doesn't speak much and seems to be a bit slow in understanding.
        ```
