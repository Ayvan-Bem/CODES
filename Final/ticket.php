<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"> 
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style2.css">
  <link rel="shortcut icon" href="C:\xampp\htdocs\images\phonto.jpg" type="image/x-icon">
  <title>Ticket Reservation</title>
</head>
  <body style="background-image:url(./images/MOA.jpg)">
    <header><div class="icon">
      <img src="./images/Contix.png" />
    </div>
  </header>
    <section id="Locations">
      <div class="Locations container">
        <div class="Location-top">
          <h1 class="section-title">Dec<span>e</span>mber</h1>
          <div class="win-grid">
            <p class="week" id="1">Mo</p>
            <p class="week" id="2">Tu</p>
            <p class="week" id="3">We</p>
            <p class="week" id="4">Th</p>
            <p class="week" id="5">Fr</p>
            <p class="week" id="6">Sa</p>
            <p class="week" id="7">Su</p>
            <div class="win-btn win-btn-inactive" id="40">29</div>
            <div class="win-btn win-btn-inactive" id="41">30</div>
            <div class="win-btn win-btn-inactive" id="42">31</div>
            <div class="win-btn" id="1">1</div>
            <div class="win-btn" id="2">2</div>
            <div class="win-btn" id="3">3</div>
            <div class="win-btn" id="4">4</div>
            <div class="win-btn" id="5">5</div>
            <div class="win-btn" id="6">6</div>
            <div class="win-btn" id="7">7</div>
            <div class="win-btn" id="8">8</div>
            <div class="win-btn" id="9">9</div>
            <div class="win-btn" id="10">10</div>
            <div class="win-btn" id="11">11</div>
            <div class="win-btn" id="12">12</div>
            <div class="win-btn win-btn-active-1" id="13">13</div>
            <div class="win-btn win-btn-active-2" id="14">14</div>
            <div class="win-btn win-btn-active-3" id="15">15</div>
            <div class="win-btn win-btn-active-4" id="16">16</div>
            <div class="win-btn win-btn-active-5" id="17">17</div>
            <div class="win-btn" id="18">18</div>
            <div class="win-btn" id="19">19</div>
            <div class="win-btn" id="20">20</div>
            <div class="win-btn" id="21">21</div>
            <div class="win-btn" id="22">22</div>
            <div class="win-btn" id="23">23</div>
            <div class="win-btn" id="24">24</div>
            <div class="win-btn" id="25">25</div>
            <div class="win-btn" id="26">26</div>
            <div class="win-btn" id="27">27</div>
            <div class="win-btn" id="28">28</div>
            <div class="win-btn" id="29">29</div>
            <div class="win-btn" id="30">30</div>
            <div class="win-btn win-btn-inactive" id="31">1</div>
            <div class="win-btn win-btn-inactive" id="32">2</div>
            <div class="win-btn win-btn-inactive" id="33">3</div>
            <div class="win-btn win-btn-inactive" id="34">4</div>
            <div class="win-btn win-btn-inactive" id="35">5</div>
            <div class="win-btn win-btn-inactive" id="36">6</div>
            <div class="win-btn win-btn-inactive" id="37">7</div>
            <div class="win-btn win-btn-inactive" id="38">8</div>
            <div class="win-btn win-btn-inactive" id="39">9</div>
            </div>
           </div>
        </div>
        
      </section>
   <article> 
        <div class="Location-bottom">
          <div class="Location-item">
              <form action="connect.php" method="POST">
              <div class="elem-group">
                <label for="name">Your Name</label>
                <input type="text" name="Name" placeholder="Eibrhm Toledo">
              </div>
              <div class="elem-group">
                <label for="phone">Your Phone</label>
                <input type="tel" name="Number" placeholder="+63999-748-5467">
              </div>
              <div class="elem-group">
                <label for="Concert">Select Concert</label>
                <select name="Concert" >
                  <option value="NA">Select</option>
                    <option value="BlackPink">BlackPink (PINK)</option>
                    <option value="Twice">Twice(VIOLET)</option>
                    <option value="Taylor Swift">Taylor Swift (BLUE)</option>
                    <option value="Harry Styles">Harry Styles(GREEN)</option>
                    <option value="Justin Bieber">Justin Bieber(YELLOW)  </option>
                </select>
                <label for="Seat">Select Box</label>
                <select name="BOX" >
                  <option value="NA">Select</option>
                    <option value="VIP">VIP</option>
                    <option value="Back Stage">Back Stage</option>
                    <option value="Lower Box">Lower Box</option>
                    <option value="Upper Box">Upper Box</option>
                    <option value="Celebrity Box">Celebrity Box</option>
                    <option value="Economy Box">Economy Box</option>
                </select>
                <label for="Location">Location</label>
                <select name="Location" >
                  <option value="Moa Arena">Moa Arena</option>
                </select>
              </div>
            <hr>
            <button type="Submit" name="Submit" value="Add" >Submit</button> 
              </body>
            </form>
        </div>
      </div>
    </article>  

      <script>
        const offset = 69;
    const borderWidth = 3;
    const angles = []; //in  rad
    for (let i = 0; i <= 2; i += 0.25) {
      angles.push(Math.PI * i);
    }
    let nearBy = [];
    let activeBtn = document.querySelector(".win-btn-active");
    let lastClicked = null;
    
    document.querySelectorAll(".win-btn").forEach((btn) => {
      btn.onclick = (e) => {
        //clear effects from last clicked date and set lastClicked to current item
        if (lastClicked) {
          lastClicked.classList.remove("win-btn-selected");
        }
        lastClicked = e.currentTarget;
    
        activeBtn.classList.toggle(
          "win-btn-active-unselected",
          e.currentTarget.id !== activeBtn.id
        );
        e.currentTarget.classList.add("win-btn-selected");
      };
    });
    
    function clearNearBy() {
      nearBy.splice(0).forEach((e) => (e.style.borderImage = null));
    }
    
    const body = document.querySelector(".win-grid");
    
    body.addEventListener("mousemove", (e) => {
      let x = e.clientX; //x position of cursor.
      let y = e.clientY; //y position of cursor
    
      clearNearBy();
    
      nearBy = angles.reduce((acc, rad, index, arr) => {
        const offsets = [offset * 0.35, offset * 1.105];
    
        const elements = offsets.reduce((elementAccumulator, o, i, offsetArray) => {
          //to skip the intermediate first points calculation
          // if (index % 2 === 0 && i === 0) return elementAccumulator;
          const cx = Math.floor(x + Math.cos(rad) * o);
          const cy = Math.floor(y + Math.sin(rad) * o);
          const element = document.elementFromPoint(cx, cy);
    
          if (
            element &&
            element.classList.contains("win-btn") &&
            !element.classList.contains("win-btn-active") &&
            !element.classList.contains("win-btn-selected") &&
            elementAccumulator.findIndex((ae) => ae.id === element.id) < 0
          ) {
            const brect = element.getBoundingClientRect();
            const bx = x - brect.left; //x position within the element.
            const by = y - brect.top; //y position within the element.
            const gr = Math.floor(offset * 1.7);
            if (!element.style.borderImage)
              element.style.borderImage = `radial-gradient(${gr}px ${gr}px at ${bx}px ${by}px ,rgba(255,255,255,0.3),rgba(255,255,255,0.1),transparent ) 9 / ${borderWidth}px / 0px stretch `;
            console.log("element at", offsets, (rad * 180) / Math.PI, element);
    
            return [...elementAccumulator, element];
          }
          return elementAccumulator;
        }, []);
    
        return acc.concat(elements);
      }, []);
    });
    
    body.onmouseleave = (e) => {
      clearNearBy();
    };
      </script>
        
        
    


</body>