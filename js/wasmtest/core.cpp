#include <SDL2/SDL.h>
#include <emscripten.h>
#include <cstdlib>

struct context
{
    SDL_Renderer *renderer;
    int iteration;
};

int note_played = NULL;

void mainloop(void *arg)
{
    context *ctx = static_cast<context*>(arg);
    SDL_Renderer *renderer = ctx->renderer;

    // example: draw a moving rectangle

    // red background
    SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
    SDL_RenderClear(renderer);

    // moving blue rectangle
    SDL_Rect r;
    r.x = ctx->iteration % 255;
    r.y = 50;
    r.w = 50;
    r.h = 50;
    if (note_played % 2 == 0) {
        SDL_SetRenderDrawColor(renderer, 0, 0, 255, 255 );
    } else {
        SDL_SetRenderDrawColor(renderer, 0, 255, 0, 255 );
    }

    SDL_RenderFillRect(renderer, &r );

    SDL_RenderPresent(renderer);

    ctx->iteration++;
}

extern "C" {
  int set_note_played(int noteIndex) {
    note_played = noteIndex;
    printf("set_note_played(%d)\n", noteIndex);
    return 0;
  }
}

int main()
{
    printf("Hello World\n");


    SDL_Init(SDL_INIT_VIDEO);
    SDL_Window *window;
    SDL_Renderer *renderer;
    SDL_CreateWindowAndRenderer(600, 400, 0, &window, &renderer);

    context ctx;
    ctx.renderer = renderer;
    ctx.iteration = 0;

    const int simulate_infinite_loop = 1; // call the function repeatedly
    const int fps = -1; // call the function as fast as the browser wants to render (typically 60fps)
    emscripten_set_main_loop_arg(mainloop, &ctx, fps, simulate_infinite_loop);

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return EXIT_SUCCESS;
}
